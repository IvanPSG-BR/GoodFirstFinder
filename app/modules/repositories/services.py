import math
import uuid

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.exceptions import NotFoundException
from app.common.schemas import PaginatedResponse
from app.modules.repositories.models import Repository
from app.modules.repositories.schemas import RepoCreate, RepoResponse


async def list_repositories(
    db: AsyncSession,
    page: int = 1,
    per_page: int = 20,
    language: str | None = None,
) -> PaginatedResponse[RepoResponse]:
    query = select(Repository).where(Repository.is_active == True)  # noqa: E712
    if language:
        query = query.where(Repository.language == language)

    total_result = await db.execute(select(func.count()).select_from(query.subquery()))
    total = total_result.scalar_one()

    query = query.offset((page - 1) * per_page).limit(per_page)
    result = await db.execute(query)
    items = result.scalars().all()

    return PaginatedResponse(
        items=[RepoResponse.model_validate(r) for r in items],
        total=total,
        page=page,
        per_page=per_page,
        pages=math.ceil(total / per_page) if total else 0,
    )


async def get_repository_by_id(db: AsyncSession, repo_id: uuid.UUID) -> RepoResponse:
    result = await db.execute(select(Repository).where(Repository.id == repo_id))
    repo = result.scalar_one_or_none()
    if not repo:
        raise NotFoundException("Repository", str(repo_id))
    return RepoResponse.model_validate(repo)


async def create_repository(db: AsyncSession, data: RepoCreate) -> RepoResponse:
    repo = Repository(**data.model_dump())
    db.add(repo)
    await db.commit()
    await db.refresh(repo)
    return RepoResponse.model_validate(repo)
