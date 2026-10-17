"""LLM Provider abstractions for Step 8."""

from __future__ import annotations

import logging
import time
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from config.settings import get_settings
from rag.generation.models import GeneratedAnswer
from rag.context.models import AssembledContext

logger = logging.getLogger(__name__)


class BaseLLMProvider(ABC):
    """Abstract interface for LLM providers."""
    
    @abstractmethod
    def get_name(self) -> str:
        """Return the name of the provider."""
        pass
        
    @abstractmethod
    def generate(
        self, 
        prompt: str, 
        system_prompt: Optional[str] = None, 
        temperature: float = 0.0,
        max_tokens: Optional[int] = None
    ) -> GeneratedAnswer:
        """Generate an answer synchronously from the prompt."""
        pass
        
    @abstractmethod
    def is_available(self) -> bool:
        """Check if the provider is properly configured."""
        pass


class MockLLMProvider(BaseLLMProvider):
    """Deterministic offline generation mode. 
    
    Extracts grounded facts from top Step 7 context items or returns 
    insufficient-context responses when context is empty.
    """
    
    def __init__(self, assembled_context: Optional[AssembledContext] = None):
        self.assembled_context = assembled_context
    
    def get_name(self) -> str:
        return "mock"
        
    def generate(
        self, 
        prompt: str, 
        system_prompt: Optional[str] = None, 
        temperature: float = 0.0,
        max_tokens: Optional[int] = None
    ) -> GeneratedAnswer:
        start_time = time.perf_counter()
        
        # Simulate processing time
        time.sleep(0.01)
        
        answer_text = ""
        
        if not self.assembled_context or not self.assembled_context.items:
            answer_text = "Based on the available enterprise knowledge base, there is insufficient information to answer your query."
        else:
            # Deterministically synthesize an answer from the top context item
            top_item = self.assembled_context.items[0]
            title = top_item.document_title or f"Document #{top_item.document_id}"
            snippet = top_item.text.replace('\n', ' ').strip()
            # truncate snippet for summary
            if len(snippet) > 200:
                snippet = snippet[:197] + "..."
            
            answer_text = (
                f"Based on the enterprise knowledge context provided, "
                f"specifically from '{title}' (Chunk #{top_item.chunk_index}):\n\n"
                f"{snippet}\n\n"
                f"This addresses your query grounded strictly in the provided document."
            )
            
        latency = (time.perf_counter() - start_time) * 1000.0
        
        return GeneratedAnswer(
            answer=answer_text,
            raw_text=answer_text,
            prompt_tokens=len(prompt) // 4,
            completion_tokens=len(answer_text) // 4,
            total_tokens=(len(prompt) + len(answer_text)) // 4,
            model_name="mock-deterministic",
            provider_name="mock",
            latency_ms=latency,
            finish_reason="stop",
            is_mock=True
        )
        
    def is_available(self) -> bool:
        return True


class GeminiLLMProvider(BaseLLMProvider):
    """Google Gemini provider via Google GenAI SDK."""
    
    def __init__(self, api_key: str, model_name: str):
        self.api_key = api_key
        self.model_name = model_name
        self._client = None
        
    def _get_client(self):
        try:
            from google import genai
            if not self._client:
                self._client = genai.Client(api_key=self.api_key)
            return self._client
        except ImportError:
            logger.error("google-genai SDK is not installed.")
            raise
            
    def get_name(self) -> str:
        return "gemini"
        
    def generate(
        self, 
        prompt: str, 
        system_prompt: Optional[str] = None, 
        temperature: float = 0.0,
        max_tokens: Optional[int] = None
    ) -> GeneratedAnswer:
        start_time = time.perf_counter()
        
        client = self._get_client()
        from google.genai import types
        
        config = types.GenerateContentConfig(
            temperature=temperature,
            system_instruction=system_prompt,
            max_output_tokens=max_tokens
        )
        
        response = client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=config,
        )
        
        latency = (time.perf_counter() - start_time) * 1000.0
        
        usage = getattr(response, "usage_metadata", None)
        pt = usage.prompt_token_count if usage else None
        ct = usage.candidates_token_count if usage else None
        tt = usage.total_token_count if usage else None
        
        return GeneratedAnswer(
            answer=response.text,
            raw_text=response.text,
            prompt_tokens=pt,
            completion_tokens=ct,
            total_tokens=tt,
            model_name=self.model_name,
            provider_name=self.get_name(),
            latency_ms=latency,
            finish_reason="stop",
            is_mock=False
        )
        
    def is_available(self) -> bool:
        return bool(self.api_key)


class OpenAICompatibleProvider(BaseLLMProvider):
    """OpenAI-compatible / OpenRouter API provider."""
    
    def __init__(self, api_key: str, base_url: str, model_name: str):
        self.api_key = api_key
        self.base_url = base_url
        self.model_name = model_name
        self._client = None
        
    def _get_client(self):
        try:
            from openai import OpenAI
            if not self._client:
                self._client = OpenAI(api_key=self.api_key, base_url=self.base_url)
            return self._client
        except ImportError:
            logger.error("openai SDK is not installed.")
            raise
            
    def get_name(self) -> str:
        return "openai_compatible"
        
    def generate(
        self, 
        prompt: str, 
        system_prompt: Optional[str] = None, 
        temperature: float = 0.0,
        max_tokens: Optional[int] = None
    ) -> GeneratedAnswer:
        start_time = time.perf_counter()
        
        client = self._get_client()
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        response = client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        latency = (time.perf_counter() - start_time) * 1000.0
        
        choice = response.choices[0]
        answer = choice.message.content
        
        pt = response.usage.prompt_tokens if response.usage else None
        ct = response.usage.completion_tokens if response.usage else None
        tt = response.usage.total_tokens if response.usage else None
        
        return GeneratedAnswer(
            answer=answer or "",
            raw_text=answer or "",
            prompt_tokens=pt,
            completion_tokens=ct,
            total_tokens=tt,
            model_name=self.model_name,
            provider_name=self.get_name(),
            latency_ms=latency,
            finish_reason=choice.finish_reason,
            is_mock=False
        )
        
    def is_available(self) -> bool:
        return bool(self.api_key)


class LocalLLMProvider(BaseLLMProvider):
    """Local LLM provider utilizing Ollama."""
    
    def __init__(self, base_url: str, model_name: str, assembled_context: Optional[AssembledContext] = None):
        self.base_url = base_url
        self.model_name = model_name
        self.assembled_context = assembled_context
        self._client = None
        
    def _get_client(self):
        try:
            from openai import OpenAI
            if not self._client:
                # Local Ollama client doesn't need a real API key
                self._client = OpenAI(api_key="ollama", base_url=self.base_url)
            return self._client
        except ImportError:
            logger.error("openai SDK is not installed.")
            raise
            
    def get_name(self) -> str:
        return "local"
        
    def generate(
        self, 
        prompt: str, 
        system_prompt: Optional[str] = None, 
        temperature: float = 0.0,
        max_tokens: Optional[int] = None
    ) -> GeneratedAnswer:
        start_time = time.perf_counter()
        
        if not self.assembled_context or not self.assembled_context.items:
            # Prevent hallucination explicitly
            answer_text = "I don't have enough information in the available enterprise knowledge base to answer this reliably."
            latency = (time.perf_counter() - start_time) * 1000.0
            return GeneratedAnswer(
                answer=answer_text,
                raw_text=answer_text,
                prompt_tokens=0,
                completion_tokens=0,
                total_tokens=0,
                model_name=self.model_name,
                provider_name=self.get_name(),
                latency_ms=latency,
                finish_reason="stop",
                is_mock=False
            )
            
        client = self._get_client()
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        kwargs = {
            "model": self.model_name,
            "messages": messages,
            "temperature": temperature,
        }
        if max_tokens is not None:
            kwargs["max_tokens"] = max_tokens

        try:
            response = client.chat.completions.create(**kwargs)
        except Exception as e:
            logger.error(f"Local LLM connection error: {e}")
            raise RuntimeError("Local LLM service is unavailable. Please start Ollama and verify the configured model.") from e
            
        latency = (time.perf_counter() - start_time) * 1000.0
        
        choice = response.choices[0]
        answer = choice.message.content
        
        pt = response.usage.prompt_tokens if response.usage else None
        ct = response.usage.completion_tokens if response.usage else None
        tt = response.usage.total_tokens if response.usage else None
        
        return GeneratedAnswer(
            answer=answer or "",
            raw_text=answer or "",
            prompt_tokens=pt,
            completion_tokens=ct,
            total_tokens=tt,
            model_name=self.model_name,
            provider_name=self.get_name(),
            latency_ms=latency,
            finish_reason=choice.finish_reason,
            is_mock=False
        )
        
    def is_available(self) -> bool:
        return True


class ProviderFactory:
    """Dynamic provider selection from settings or explicit request."""
    
    @staticmethod
    def get_provider(
        provider_name: Optional[str] = None, 
        assembled_context: Optional[AssembledContext] = None
    ) -> BaseLLMProvider:
        """Return the appropriate LLM provider."""
        settings = get_settings()
        
        effective_provider = provider_name or settings.llm_provider
        
        if effective_provider == "mock":
            return MockLLMProvider(assembled_context=assembled_context)
            
        if effective_provider == "local":
            return LocalLLMProvider(
                base_url=settings.local_llm_base_url,
                model_name=settings.local_llm_model,
                assembled_context=assembled_context
            )
        
        if effective_provider == "gemini":
            if not settings.gemini_api_key or not settings.gemini_api_key.get_secret_value():
                raise ValueError("GEMINI_API_KEY is not configured.")
            return GeminiLLMProvider(
                api_key=settings.gemini_api_key.get_secret_value(),
                model_name=settings.gemini_model
            )
            
        if effective_provider == "openrouter":
            # Just an example using OpenAICompatibleProvider
            key = (settings.gemini_api_key.get_secret_value() if settings.gemini_api_key else "")
            if not key or not key.startswith("sk-or-"):
                raise ValueError("OpenRouter API key is not configured.")
            return OpenAICompatibleProvider(
                api_key=key,
                base_url=settings.openrouter_base_url,
                model_name=settings.gemini_openrouter_model
            )
            
        raise ValueError(f"Unknown provider: {effective_provider}")
