import uuid

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.schemas import PaginatedResponse
from app.core.database import get_db
from app.modules.repositories import services
from app.modules.repositories.schemas import RepoResponse

router = APIRouter(prefix="/repos", tags=["repositories"])


@router.get("/", response_model=PaginatedResponse[RepoResponse])
async def list_repositories(
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100),
    language: str | None = Query(None),
    db: AsyncSession = Depends(get_db),
) -> PaginatedResponse[RepoResponse]:
    return await services.list_repositories(
        db=db, page=page, per_page=per_page, language=language
    )


@router.get("/{repo_id}", response_model=RepoResponse)
async def get_repository(
    repo_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
) -> RepoResponse:
    return await services.get_repository_by_id(db=db, repo_id=repo_id)
