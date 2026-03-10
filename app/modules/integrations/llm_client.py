import httpx

from app.common.exceptions import ExternalServiceException
from app.core.config import settings


class LLMClient:
    """Client for OpenAI-compatible LLM APIs."""

    def __init__(self) -> None:
        self._client = httpx.Client(
            base_url=settings.OPENAI_BASE_URL,
            headers={"Authorization": f"Bearer {settings.OPENAI_API_KEY}"},
            timeout=60.0,
        )
        self._model = settings.OPENAI_MODEL

    def analyze_repository(self, context: dict) -> str:
        """Analyze a repository context and return a friendliness justification."""
        prompt = self._build_prompt(context)
        try:
            response = self._client.post(
                "/chat/completions",
                json={
                    "model": self._model,
                    "messages": [
                        {
                            "role": "system",
                            "content": (
                                "You are an expert Open Source curator. "
                                "Analyze the repository data and produce a brief, "
                                "helpful justification for beginner developers explaining "
                                "why this project is (or isn't) beginner-friendly."
                            ),
                        },
                        {"role": "user", "content": prompt},
                    ],
                    "max_tokens": 256,
                    "temperature": 0.3,
                },
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"].strip()
        except httpx.HTTPStatusError as exc:
            raise ExternalServiceException("LLM", str(exc)) from exc

    @staticmethod
    def _build_prompt(context: dict) -> str:
        return (
            f"Repository: {context.get('full_name')}\n"
            f"Description: {context.get('description', 'N/A')}\n"
            f"Language: {context.get('language', 'N/A')}\n"
            f"Stars: {context.get('stars_count', 0)}\n"
            f"Open Issues: {context.get('open_issues_count', 0)}\n"
            f"Has CONTRIBUTING.md: {context.get('has_contributing', False)}\n"
            f"Has CODE_OF_CONDUCT.md: {context.get('has_code_of_conduct', False)}\n\n"
            "Provide a short (2-3 sentences) beginner-friendly justification."
        )

    def __del__(self) -> None:
        self._client.close()
