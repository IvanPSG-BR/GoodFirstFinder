import uuid
from datetime import datetime

from pydantic import BaseModel


class ScoreCriteriaResponse(BaseModel):
    id: uuid.UUID
    criterion_name: str
    criterion_value: float
    weight: float

    model_config = {"from_attributes": True}


class ScoreResponse(BaseModel):
    id: uuid.UUID
    repository_id: uuid.UUID
    total_score: float
    documentation_score: float
    community_score: float
    activity_score: float
    beginner_friendliness_score: float
    justification: str | None
    created_at: datetime
    updated_at: datetime
    criteria: list[ScoreCriteriaResponse] = []

    model_config = {"from_attributes": True}
