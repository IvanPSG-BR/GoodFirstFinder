from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.modules.search import services
from app.modules.search.schemas import SearchFilters, SearchResponse

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/", response_model=SearchResponse)
async def search_repositories(
    filters: SearchFilters = Depends(),
    db: AsyncSession = Depends(get_db),
) -> SearchResponse:
    return await services.search_repositories(db=db, filters=filters)
