from unittest.mock import MagicMock, patch

import pytest

from app.common.exceptions import ExternalServiceException
from app.modules.integrations.github_client import GitHubClient


class TestGitHubClient:
    @patch("app.modules.integrations.github_client.httpx.Client")
    def test_get_repository_success(self, mock_client_class):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": 123,
            "full_name": "owner/repo",
            "name": "repo",
            "description": "A test repo",
            "language": "Python",
            "html_url": "https://github.com/owner/repo",
            "stargazers_count": 50,
            "forks_count": 5,
            "open_issues_count": 10,
            "archived": False,
            "default_branch": "main",
        }
        mock_response.raise_for_status = MagicMock()

        mock_client = MagicMock()
        mock_client.get.return_value = mock_response
        mock_client_class.return_value = mock_client

        client = GitHubClient()
        repo = client.get_repository("owner/repo")

        assert repo.full_name == "owner/repo"
        assert repo.id == 123
        assert repo.language == "Python"

    @patch("app.modules.integrations.github_client.httpx.Client")
    def test_get_repository_raises_on_http_error(self, mock_client_class):
        import httpx

        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
            "Not Found", request=MagicMock(), response=MagicMock()
        )

        mock_client = MagicMock()
        mock_client.get.return_value = mock_response
        mock_client_class.return_value = mock_client

        client = GitHubClient()
        with pytest.raises(ExternalServiceException):
            client.get_repository("owner/nonexistent")

    @patch("app.modules.integrations.github_client.httpx.Client")
    def test_check_file_exists_true(self, mock_client_class):
        mock_response = MagicMock()
        mock_response.status_code = 200

        mock_client = MagicMock()
        mock_client.get.return_value = mock_response
        mock_client_class.return_value = mock_client

        client = GitHubClient()
        assert client.check_file_exists("owner/repo", "CONTRIBUTING.md") is True

    @patch("app.modules.integrations.github_client.httpx.Client")
    def test_check_file_exists_false(self, mock_client_class):
        mock_response = MagicMock()
        mock_response.status_code = 404

        mock_client = MagicMock()
        mock_client.get.return_value = mock_response
        mock_client_class.return_value = mock_client

        client = GitHubClient()
        assert client.check_file_exists("owner/repo", "MISSING.md") is False
