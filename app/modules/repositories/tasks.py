"""
Background ingestion tasks for repositories.

These are plain functions invoked by the CLI ingestion script
(python -m app.ingest). No task queue required.
"""


def fetch_repo_data(repo_full_name: str) -> dict:
    """Fetch repository data from GitHub API and persist it."""
    from app.modules.integrations.github_client import GitHubClient  # noqa: PLC0415

    client = GitHubClient()
    return client.get_repository(repo_full_name).model_dump()


def sync_repo_status(repo_full_name: str) -> dict:
    """Sync repository status (archived, open issues, etc.) from GitHub."""
    from app.modules.integrations.github_client import GitHubClient  # noqa: PLC0415

    client = GitHubClient()
    return client.get_repository(repo_full_name).model_dump()
