import uuid

from sqlalchemy import Float, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.common.models import TimestampMixin
from app.core.database import Base


class Score(Base, TimestampMixin):
    __tablename__ = "scores"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    repository_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("repositories.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
        index=True,
    )
    total_score: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    documentation_score: Mapped[float] = mapped_column(Float, default=0.0)
    community_score: Mapped[float] = mapped_column(Float, default=0.0)
    activity_score: Mapped[float] = mapped_column(Float, default=0.0)
    beginner_friendliness_score: Mapped[float] = mapped_column(Float, default=0.0)
    justification: Mapped[str | None] = mapped_column(Text, nullable=True)


class ScoreCriteria(Base, TimestampMixin):
    __tablename__ = "score_criteria"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    score_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("scores.id", ondelete="CASCADE"),
        nullable=False,
    )
    criterion_name: Mapped[str] = mapped_column(String(100), nullable=False)
    criterion_value: Mapped[float] = mapped_column(Float, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False, default=1.0)
