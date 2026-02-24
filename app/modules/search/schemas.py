from pydantic import BaseModel, Field


class SearchFilters(BaseModel):
    query: str | None = Field(None, description="Free text search")
    language: str | None = Field(None, description="Programming language filter")
    min_score: float | None = Field(None, ge=0.0, le=10.0, description="Minimum friendliness score")
    max_score: float | None = Field(None, ge=0.0, le=10.0, description="Maximum friendliness score")
    has_contributing: bool | None = Field(None, description="Has CONTRIBUTING.md")
    has_code_of_conduct: bool | None = Field(None, description="Has CODE_OF_CONDUCT.md")
    page: int = Field(1, ge=1)
    per_page: int = Field(20, ge=1, le=100)


class SearchResultItem(BaseModel):
    repo_id: str
    full_name: str
    description: str | None
    language: str | None
    stars_count: int
    html_url: str
    total_score: float | None
    justification: str | None

    model_config = {"from_attributes": True}


class SearchResponse(BaseModel):
    items: list[SearchResultItem]
    total: int
    page: int
    per_page: int
    pages: int
