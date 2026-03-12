import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.exceptions import NotFoundException
from app.modules.scoring.models import Score
from app.modules.scoring.schemas import ScoreResponse


async def get_score_by_repo_id(
    db: AsyncSession, repository_id: uuid.UUID
) -> ScoreResponse:
    result = await db.execute(
        select(Score).where(Score.repository_id == repository_id)
    )
    score = result.scalar_one_or_none()
    if not score:
        raise NotFoundException("Score", str(repository_id))
    return ScoreResponse.model_validate(score)


def calculate_total_score(
    documentation: float,
    community: float,
    activity: float,
    beginner_friendliness: float,
    weights: dict[str, float] | None = None,
) -> float:
    if weights is None:
        weights = {
            "documentation": 0.30,
            "community": 0.20,
            "activity": 0.20,
            "beginner_friendliness": 0.30,
        }
    total = (
        documentation * weights["documentation"]
        + community * weights["community"]
        + activity * weights["activity"]
        + beginner_friendliness * weights["beginner_friendliness"]
    )
    return round(min(max(total, 0.0), 10.0), 2)
