from datetime import datetime

from pydantic import BaseModel, Field


class GitHubRepo(BaseModel):
    id: int
    full_name: str
    name: str
    description: str | None
    language: str | None
    html_url: str
    stargazers_count: int
    forks_count: int
    open_issues_count: int
    archived: bool
    default_branch: str = "main"


class GitHubIssue(BaseModel):
    id: int
    number: int
    title: str
    body: str | None
    state: str
    html_url: str
    labels: list[dict] = []
    created_at: datetime
    updated_at: datetime


class GitHubPullRequest(BaseModel):
    id: int
    number: int
    title: str
    state: str
    html_url: str
    created_at: datetime
    merged_at: datetime | None = None
