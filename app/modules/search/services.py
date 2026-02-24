import math

from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.repositories.models import Repository
from app.modules.scoring.models import Score
from app.modules.search.schemas import SearchFilters, SearchResponse, SearchResultItem


async def search_repositories(
    db: AsyncSession, filters: SearchFilters
) -> SearchResponse:
    query = (
        select(
            Repository.id,
            Repository.full_name,
            Repository.description,
            Repository.language,
            Repository.stars_count,
            Repository.html_url,
            Repository.has_contributing,
            Repository.has_code_of_conduct,
            Score.total_score,
            Score.justification,
        )
        .outerjoin(Score, Score.repository_id == Repository.id)
        .where(Repository.is_active == True)  # noqa: E712
        .where(Repository.is_archived == False)  # noqa: E712
    )

    conditions = []

    if filters.language:
        conditions.append(Repository.language == filters.language)

    if filters.has_contributing is not None:
        conditions.append(Repository.has_contributing == filters.has_contributing)

    if filters.has_code_of_conduct is not None:
        conditions.append(Repository.has_code_of_conduct == filters.has_code_of_conduct)

    if filters.min_score is not None:
        conditions.append(Score.total_score >= filters.min_score)

    if filters.max_score is not None:
        conditions.append(Score.total_score <= filters.max_score)

    if filters.query:
        conditions.append(
            Repository.full_name.ilike(f"%{filters.query}%")
            | Repository.description.ilike(f"%{filters.query}%")
        )

    if conditions:
        query = query.where(and_(*conditions))

    query = query.order_by(Score.total_score.desc().nullslast())

    result = await db.execute(query)
    rows = result.all()
    total = len(rows)

    start = (filters.page - 1) * filters.per_page
    end = start + filters.per_page
    page_rows = rows[start:end]

    items = [
        SearchResultItem(
            repo_id=str(row.id),
            full_name=row.full_name,
            description=row.description,
            language=row.language,
            stars_count=row.stars_count,
            html_url=row.html_url,
            total_score=row.total_score,
            justification=row.justification,
        )
        for row in page_rows
    ]

    return SearchResponse(
        items=items,
        total=total,
        page=filters.page,
        per_page=filters.per_page,
        pages=math.ceil(total / filters.per_page) if total else 0,
    )
