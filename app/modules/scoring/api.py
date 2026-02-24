import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.modules.scoring import services
from app.modules.scoring.schemas import ScoreResponse

router = APIRouter(prefix="/scores", tags=["scoring"])


@router.get("/{repo_id}", response_model=ScoreResponse)
async def get_score(
    repo_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
) -> ScoreResponse:
    return await services.get_score_by_repo_id(db=db, repository_id=repo_id)
