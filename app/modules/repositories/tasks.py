from app.core.celery_config import celery_app


@celery_app.task(name="repositories.fetch_repo_data", bind=True, max_retries=3)
def fetch_repo_data(self, repo_full_name: str) -> dict:
    """Fetch repository data from GitHub API and persist it."""
    try:
        from app.modules.integrations.github_client import GitHubClient  # noqa: PLC0415

        client = GitHubClient()
        return client.get_repository(repo_full_name)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60) from exc


@celery_app.task(name="repositories.sync_repo_status", bind=True, max_retries=3)
def sync_repo_status(self, repo_full_name: str) -> dict:
    """Sync repository status (archived, open issues, etc.) from GitHub."""
    try:
        from app.modules.integrations.github_client import GitHubClient  # noqa: PLC0415

        client = GitHubClient()
        return client.get_repository(repo_full_name)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=120) from exc
