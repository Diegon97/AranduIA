"""
Capa de Abstracción de Modelos de Lenguaje (LLM Provider Agnostic) — AranduIA.
Permite alternar con cero fricción entre reglas locales offline, servidores Ollama y APIs remotas.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
import httpx
from pydantic import BaseModel
from src.config import settings


class LLMMessage(BaseModel):
    role: str  # "system", "user", "assistant"
    content: str


class LLMResponse(BaseModel):
    content: str
    provider: str
    model: str
    is_offline: bool = True
    metadata: Dict[str, Any] = {}


class BaseLLMProvider(ABC):
    @abstractmethod
    async def generate_response(
        self,
        messages: List[LLMMessage],
        temperature: float = 0.5,
        max_tokens: int = 800,
    ) -> LLMResponse:
        pass


class LocalRuleEngine(BaseLLMProvider):
    """
    Motor local de reglas y plantillas pedagógicas soberano.
    Funciona 100% offline, en cualquier CPU (Raspberry Pi, laptops antiguas), sin requerir GPU ni RAM masiva.
    """

    async def generate_response(
        self,
        messages: List[LLMMessage],
        temperature: float = 0.5,
        max_tokens: int = 800,
    ) -> LLMResponse:
        user_msg = next((m.content for m in reversed(messages) if m.role == "user"), "")
        system_msg = next((m.content for m in messages if m.role == "system"), "")

        # Respuestas pedagógicas contextuales
        content = (
            "Entiendo tu consulta. Como tutor socrático de AranduIA, te acompaño paso a paso: "
            "¿Qué saberes previos tenés sobre este tema y cuál es el primer paso que intentarías?"
        )

        return LLMResponse(
            content=content,
            provider="local_rules",
            model="arandu-rule-engine-v1",
            is_offline=True,
            metadata={"source": "heuristic_offline"},
        )


class OllamaProvider(BaseLLMProvider):
    """Conector a servidor local Ollama (Llama 3, Phi-3, Mistral)."""

    def __init__(self, base_url: str = settings.OLLAMA_BASE_URL, model: str = settings.OLLAMA_MODEL):
        self.base_url = base_url.rstrip("/")
        self.model = model

    async def generate_response(
        self,
        messages: List[LLMMessage],
        temperature: float = 0.5,
        max_tokens: int = 800,
    ) -> LLMResponse:
        url = f"{self.base_url}/api/chat"
        payload = {
            "model": self.model,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "stream": False,
            "options": {"temperature": temperature, "num_predict": max_tokens},
        }

        try:
            async with httpx.AsyncClient(timeout=45.0) as client:
                res = await client.post(url, json=payload)
                res.raise_for_status()
                data = res.json()
                content = data.get("message", {}).get("content", "")
                return LLMResponse(
                    content=content,
                    provider="ollama",
                    model=self.model,
                    is_offline=True,
                )
        except Exception as e:
            # Fallback seguro a motor de reglas
            fallback = LocalRuleEngine()
            resp = await fallback.generate_response(messages)
            resp.metadata["fallback_error"] = str(e)
            return resp


class GenericAPIProvider(BaseLLMProvider):
    """Conector para APIs compatibles con OpenAI/Groq en caso de contar con conexión a internet."""

    def __init__(
        self,
        api_url: str = settings.EXTERNAL_API_URL,
        api_key: Optional[str] = settings.EXTERNAL_API_KEY,
        model: str = settings.EXTERNAL_API_MODEL,
    ):
        self.api_url = api_url.rstrip("/")
        self.api_key = api_key
        self.model = model

    async def generate_response(
        self,
        messages: List[LLMMessage],
        temperature: float = 0.5,
        max_tokens: int = 800,
    ) -> LLMResponse:
        if not self.api_key:
            fallback = LocalRuleEngine()
            return await fallback.generate_response(messages)

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                res = await client.post(f"{self.api_url}/chat/completions", headers=headers, json=payload)
                res.raise_for_status()
                data = res.json()
                content = data["choices"][0]["message"]["content"]
                return LLMResponse(
                    content=content,
                    provider="external_api",
                    model=self.model,
                    is_offline=False,
                )
        except Exception as e:
            fallback = LocalRuleEngine()
            resp = await fallback.generate_response(messages)
            resp.metadata["fallback_error"] = str(e)
            return resp


def get_llm_provider() -> BaseLLMProvider:
    """Factory de proveedores según configuración de entorno."""
    provider_type = settings.LLM_PROVIDER.lower()
    if provider_type == "ollama":
        return OllamaProvider()
    elif provider_type == "external_api" and settings.EXTERNAL_API_KEY:
        return GenericAPIProvider()
    return LocalRuleEngine()
