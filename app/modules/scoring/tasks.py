from app.core.celery_config import celery_app


@celery_app.task(name="scoring.calculate_score", bind=True, max_retries=3)
def calculate_score(self, repository_id: str) -> dict:
    """Calculate the friendliness score for a repository."""
    try:
        # TODO: Implement full scoring pipeline (LLM analysis + heuristics)
        return {"repository_id": repository_id, "status": "calculated"}
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60) from exc


@celery_app.task(name="scoring.reevaluate_repo", bind=True, max_retries=3)
def reevaluate_repo(self, repository_id: str) -> dict:
    """Re-evaluate and update the score for an existing repository."""
    try:
        return {"repository_id": repository_id, "status": "reevaluated"}
    except Exception as exc:
        raise self.retry(exc=exc, countdown=120) from exc
