import uuid
from datetime import datetime

from pydantic import BaseModel, HttpUrl


class RepoBase(BaseModel):
    full_name: str
    name: str
    owner: str
    description: str | None = None
    language: str | None = None
    html_url: str
    stars_count: int = 0
    forks_count: int = 0
    open_issues_count: int = 0
    has_contributing: bool = False
    has_code_of_conduct: bool = False
    is_archived: bool = False


class RepoCreate(RepoBase):
    github_id: int


class RepoResponse(RepoBase):
    id: uuid.UUID
    github_id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
