import httpx

from app.common.exceptions import ExternalServiceException
from app.core.config import settings
from app.modules.integrations.schemas import GitHubIssue, GitHubRepo


class GitHubClient:
    def __init__(self) -> None:
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if settings.GITHUB_TOKEN:
            headers["Authorization"] = f"Bearer {settings.GITHUB_TOKEN}"
        self._client = httpx.Client(
            base_url=settings.GITHUB_API_BASE_URL,
            headers=headers,
            timeout=30.0,
        )

    def get_repository(self, full_name: str) -> GitHubRepo:
        try:
            response = self._client.get(f"/repos/{full_name}")
            response.raise_for_status()
            return GitHubRepo.model_validate(response.json())
        except httpx.HTTPStatusError as exc:
            raise ExternalServiceException("GitHub", str(exc)) from exc

    def list_good_first_issues(
        self, full_name: str, per_page: int = 30
    ) -> list[GitHubIssue]:
        try:
            response = self._client.get(
                f"/repos/{full_name}/issues",
                params={"labels": "good first issue", "state": "open", "per_page": per_page},
            )
            response.raise_for_status()
            return [GitHubIssue.model_validate(issue) for issue in response.json()]
        except httpx.HTTPStatusError as exc:
            raise ExternalServiceException("GitHub", str(exc)) from exc

    def check_file_exists(self, full_name: str, path: str) -> bool:
        try:
            response = self._client.get(f"/repos/{full_name}/contents/{path}")
            return response.status_code == 200  # noqa: PLR2004
        except httpx.HTTPError:
            return False

    def __del__(self) -> None:
        self._client.close()
