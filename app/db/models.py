from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db import Base


class TextEntry(Base):
    __tablename__ = "entries"

    uuid = Column(
        UUID(as_uuid=True),
        primary_key=True,
        unique=True,
        nullable=False,
        default=uuid.uuid4,
    )
    text = Column(String, nullable=False)
