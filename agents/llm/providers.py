"""Common LLM provider interface and concrete provider implementations."""

from __future__ import annotations

import json
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Mapping, Sequence, TypeVar

from google import genai
from google.genai import types as genai_types
from openai import OpenAI
from pydantic import BaseModel


StructuredResponse = TypeVar("StructuredResponse", bound=BaseModel)
Message = Mapping[str, str]


class ProviderConfigurationError(RuntimeError):
    """Raised when a provider is not configured for the selected credential."""


@dataclass(frozen=True)
class LLMResponse:
    """Provider-neutral response returned by text generation calls."""

    text: str
    raw: Any = None


def is_openrouter_key(api_key: str) -> bool:
    """Identify OpenRouter credentials without exposing the credential itself."""

    return api_key.startswith("sk-or-")


def _messages_to_prompt(messages: Sequence[Message]) -> str:
    return "\n".join(f"{message.get('role', 'user')}: {message.get('content', '')}" for message in messages)


class LLMProvider(ABC):
    """Interface consumed by planner and specialist agents."""

    def __init__(self, model: str) -> None:
        self.model = model

    @abstractmethod
    def generate(self, prompt: str, *, temperature: float = 0.2) -> LLMResponse:
        raise NotImplementedError

    @abstractmethod
    def chat(self, messages: Sequence[Message], *, temperature: float = 0.2) -> LLMResponse:
        raise NotImplementedError

    @abstractmethod
    def structured(
        self,
        messages: Sequence[Message],
        response_model: type[StructuredResponse],
        *,
        temperature: float = 0.0,
    ) -> StructuredResponse:
        raise NotImplementedError

    def health_check(self) -> tuple[bool, str]:
        try:
            response = self.generate("Reply with exactly: ok", temperature=0.0)
            return bool(response.text.strip()), "ok"
        except Exception:
            return False, "inference request failed"


def extract_json(text: str) -> dict[str, Any]:
    """Extract and parse a JSON object from text using fallback strategies."""
    text = text.strip()
    
    # 1. Try direct loading
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # 2. Try markdown code block extraction
    code_block_match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    if code_block_match:
        try:
            return json.loads(code_block_match.group(1).strip())
        except json.JSONDecodeError:
            pass

    # 3. Balanced brace matching to find first JSON-like object
    start_idx = text.find("{")
    if start_idx != -1:
        brace_count = 0
        in_string = False
        escape = False
        for idx in range(start_idx, len(text)):
            char = text[idx]
            if escape:
                escape = False
                continue
            if char == "\\":
                escape = True
                continue
            if char == '"':
                in_string = not in_string
                continue
            if not in_string:
                if char == "{":
                    brace_count += 1
                elif char == "}":
                    brace_count -= 1
                    if brace_count == 0:
                        potential_json = text[start_idx : idx + 1]
                        try:
                            return json.loads(potential_json)
                        except json.JSONDecodeError:
                            pass
                        break

    raise ValueError("Could not extract a valid JSON object from the response.")


def inject_schema_instructions(messages: Sequence[Message], schema_json: str) -> list[Message]:
    """Inject detailed JSON schema validation instructions into the system message or add one."""
    instruction = (
        f"\n\n[SYSTEM INSTRUCTION: You MUST return a JSON object instance (data) conforming to the following JSON schema definition.\n"
        f"Do NOT return the schema definition itself. Return a JSON object containing the actual fields and values.\n"
        f"Schema definition:\n{schema_json}\n\n"
        f"Rules:\n"
        f"- Return ONLY the raw valid JSON object instance.\n"
        f"- Follow the provided schema exactly.\n"
        f"- Do not add extra fields.\n"
        f"- Do not return Markdown.\n"
        f"- Do not wrap JSON in ```json fences.\n"
        f"- Every required field must be present.\n"
        f"- Use correct JSON types.\n"
        f"- For lists, return JSON arrays.\n"
        f"- Never return malformed JSON.]"
    )
    
    new_messages = [dict(m) for m in messages]
    # Check if there is a system message to append to
    for msg in new_messages:
        if msg.get("role") == "system":
            msg["content"] = (msg.get("content") or "") + instruction
            return new_messages

    # If no system message found, prepend one
    new_messages.insert(0, {"role": "system", "content": instruction})
    return new_messages


class OpenAICompatibleProvider(LLMProvider):
    """Provider for NVIDIA NIM and OpenRouter's OpenAI-compatible API."""

    def __init__(self, *, api_key: str, base_url: str, model: str) -> None:
        super().__init__(model)
        self._client = OpenAI(api_key=api_key, base_url=base_url)

    def _complete(
        self,
        messages: Sequence[Message],
        *,
        temperature: float,
        response_format: bool | dict[str, Any] | None = None,
        timeout: float | None = None,
        max_tokens: int | None = 4096,
    ) -> LLMResponse:
        request: dict[str, Any] = {
            "model": self.model,
            "messages": list(messages),
            "temperature": temperature,
        }
        if response_format is True:
            request["response_format"] = {"type": "json_object"}
        elif isinstance(response_format, dict):
            request["response_format"] = response_format
        if timeout is not None:
            request["timeout"] = timeout
        if max_tokens is not None:
            request["max_tokens"] = max_tokens
            
        result = self._client.chat.completions.create(**request)
        message = result.choices[0].message
        return LLMResponse(text=message.content or "", raw=result)

    def generate(self, prompt: str, *, temperature: float = 0.2) -> LLMResponse:
        return self.chat(({"role": "user", "content": prompt},), temperature=temperature)

    def chat(self, messages: Sequence[Message], *, temperature: float = 0.2) -> LLMResponse:
        return self._complete(messages, temperature=temperature)

    def structured(
        self,
        messages: Sequence[Message],
        response_model: type[StructuredResponse],
        *,
        temperature: float = 0.0,
    ) -> StructuredResponse:
        # Build schema dynamically
        schema = response_model.model_json_schema()
        schema_json = json.dumps(schema, indent=2)

        # Prepare fallback messages with instructions
        fallback_messages = inject_schema_instructions(messages, schema_json)

        current_messages = list(messages)
        try_native = True
        response_format_arg: Any = None
        max_attempts = 3
        attempt = 0
        last_error_info = ""
        response_text = ""

        while attempt < max_attempts:
            if attempt == 0:
                if try_native:
                    # Prefer native structured outputs
                    response_format_arg = {
                        "type": "json_schema",
                        "json_schema": {
                            "name": response_model.__name__,
                            "strict": True,
                            "schema": schema,
                        },
                    }
                    current_messages = list(messages)
                else:
                    # Fallback to json_object + instructions
                    response_format_arg = {"type": "json_object"}
                    current_messages = fallback_messages
            else:
                # Retry: append previous response and correction prompt
                if len(current_messages) == len(messages):
                    current_messages = list(fallback_messages)
                
                # Append assistant content and user feedback
                current_messages.append({"role": "assistant", "content": response_text})
                correction_prompt = (
                    f"The response was invalid JSON or did not conform to the schema.\n"
                    f"Validation errors:\n{last_error_info}\n\n"
                    f"Please output the corrected JSON matching the schema exactly. "
                    f"Ensure all required fields are present and return ONLY the raw JSON string "
                    f"without markdown formatting or code blocks."
                )
                current_messages.append({"role": "user", "content": correction_prompt})
                
                # If we tried native, let's keep it if we can, else use json_object
                if response_format_arg and response_format_arg.get("type") == "json_schema":
                    pass
                else:
                    response_format_arg = {"type": "json_object"}

            try:
                # Use a 15-second timeout to prevent gateway hangs
                response = self._complete(
                    current_messages,
                    temperature=temperature,
                    response_format=response_format_arg,
                    timeout=15.0,
                )
                response_text = response.text
            except Exception as e:
                # If this is the initial attempt with native json_schema, fallback immediately
                if attempt == 0 and try_native:
                    try_native = False
                    try:
                        response_format_arg = {"type": "json_object"}
                        response = self._complete(
                            fallback_messages,
                            temperature=temperature,
                            response_format=response_format_arg,
                            timeout=15.0,
                        )
                        response_text = response.text
                    except Exception as e2:
                        response_format_arg = None
                        response = self._complete(
                            fallback_messages,
                            temperature=temperature,
                            response_format=response_format_arg,
                            timeout=15.0,
                        )
                        response_text = response.text
                else:
                    raise e

            # Parsing and Pydantic validation
            try:
                json_dict = extract_json(response_text)
                return response_model.model_validate(json_dict)
            except Exception as val_exc:
                last_error_info = str(val_exc)
                attempt += 1

        # If retries exceeded
        raise ValueError(
            f"Structured generation failed after {max_attempts} attempts.\n"
            f"Provider: OpenAICompatibleProvider\n"
            f"Model: {self.model}\n"
            f"Response Model: {response_model.__name__}\n"
            f"Error Details: {last_error_info}\n"
            f"Last Raw Response: {response_text}"
        )


class GeminiProvider(LLMProvider):
    """Native Google Gemini provider using the official google-genai SDK."""

    def __init__(self, *, api_key: str, model: str) -> None:
        super().__init__(model)
        self._client = genai.Client(api_key=api_key)

    def generate(self, prompt: str, *, temperature: float = 0.2) -> LLMResponse:
        result = self._client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=genai_types.GenerateContentConfig(temperature=temperature),
        )
        return LLMResponse(text=result.text or "", raw=result)

    def chat(self, messages: Sequence[Message], *, temperature: float = 0.2) -> LLMResponse:
        return self.generate(_messages_to_prompt(messages), temperature=temperature)

    def structured(
        self,
        messages: Sequence[Message],
        response_model: type[StructuredResponse],
        *,
        temperature: float = 0.0,
    ) -> StructuredResponse:
        result = self._client.models.generate_content(
            model=self.model,
            contents=_messages_to_prompt(messages),
            config=genai_types.GenerateContentConfig(
                temperature=temperature,
                response_mime_type="application/json",
                response_schema=response_model.model_json_schema(),
            ),
        )
        return response_model.model_validate(json.loads(result.text or "{}"))


class LocalProvider(OpenAICompatibleProvider):
    """Local LLM provider utilizing Ollama."""

    def __init__(self, *, base_url: str, model: str) -> None:
        super().__init__(api_key="ollama", base_url=base_url, model=model)

    def _complete(
        self,
        messages: Sequence[Message],
        *,
        temperature: float,
        response_format: bool | dict[str, Any] | None = None,
        timeout: float | None = None,
        max_tokens: int | None = 4096,
    ) -> LLMResponse:
        try:
            return super()._complete(
                messages,
                temperature=temperature,
                response_format=response_format,
                timeout=timeout,
                max_tokens=max_tokens,
            )
        except Exception as e:
            raise RuntimeError("LOCAL_LLM_UNAVAILABLE: Local LLM service is unavailable. Please start Ollama and verify the configured model.") from e

    def health_check(self) -> tuple[bool, str]:
        try:
            return super().health_check()
        except Exception:
            return False, "Local LLM service is unavailable"