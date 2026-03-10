"""
Background scoring tasks.

These are plain functions invoked by the CLI ingestion script
(python -m app.ingest). No task queue required.
"""


def calculate_score(repository_id: str) -> dict:
    """Calculate the friendliness score for a repository."""
    # TODO: Implement full scoring pipeline (LLM analysis + heuristics)
    return {"repository_id": repository_id, "status": "calculated"}


def reevaluate_repo(repository_id: str) -> dict:
    """Re-evaluate and update the score for an existing repository."""
    return {"repository_id": repository_id, "status": "reevaluated"}
