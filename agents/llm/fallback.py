"""Groq primary with Ollama fallback for transient failures."""

import logging
from typing import Sequence

from openai import (
    APIConnectionError,
    APITimeoutError,
    InternalServerError,
    RateLimitError,
)

from .providers import LLMProvider, LLMResponse, Message, StructuredResponse

logger = logging.getLogger(__name__)

RETRYABLE_ERRORS = (
    APIConnectionError,
    APITimeoutError,
    InternalServerError,
    RateLimitError,
)


class FallbackProvider(LLMProvider):
    """Use secondary provider when the primary has a transient failure."""

    def __init__(self, primary: LLMProvider, secondary: LLMProvider):
        super().__init__(primary.model)
        self.primary = primary
        self.secondary = secondary

    def _execute(self, method, *args, **kwargs):
        try:
            return getattr(self.primary, method)(*args, **kwargs)
        except RETRYABLE_ERRORS as exc:
            logger.warning(
                "Primary LLM unavailable (%s); using local fallback",
                type(exc).__name__,
            )
            return getattr(self.secondary, method)(*args, **kwargs)

    def generate(self, prompt: str, *, temperature: float = 0.2) -> LLMResponse:
        return self._execute("generate", prompt, temperature=temperature)

    def chat(self, messages: Sequence[Message], *, temperature: float = 0.2) -> LLMResponse:
        return self._execute("chat", messages, temperature=temperature)

    def structured(
        self,
        messages: Sequence[Message],
        response_model: type[StructuredResponse],
        *,
        temperature: float = 0.0,
    ) -> StructuredResponse:
        return self._execute(
            "structured",
            messages,
            response_model,
            temperature=temperature,
        )

    def health_check(self) -> tuple[bool, str]:
        return self.primary.health_check()
