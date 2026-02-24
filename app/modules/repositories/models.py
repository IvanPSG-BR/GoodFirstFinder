import uuid

from sqlalchemy import String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.common.models import TimestampMixin
from app.core.database import Base


class Repository(Base, TimestampMixin):
    __tablename__ = "repositories"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    github_id: Mapped[int] = mapped_column(unique=True, nullable=False, index=True)
    full_name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    owner: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    language: Mapped[str | None] = mapped_column(String(100), nullable=True, index=True)
    html_url: Mapped[str] = mapped_column(String(512), nullable=False)
    stars_count: Mapped[int] = mapped_column(default=0)
    forks_count: Mapped[int] = mapped_column(default=0)
    open_issues_count: Mapped[int] = mapped_column(default=0)
    has_contributing: Mapped[bool] = mapped_column(default=False)
    has_code_of_conduct: Mapped[bool] = mapped_column(default=False)
    is_archived: Mapped[bool] = mapped_column(default=False, index=True)
    is_active: Mapped[bool] = mapped_column(default=True, index=True)
