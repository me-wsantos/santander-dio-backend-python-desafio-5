from datetime import datetime, timezone
import uuid
from pydantic import UUID4, BaseModel, Field


def utc_now():
    return datetime.now(timezone.utc)


class BaseSchemaMixin(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=utc_now)
    udpated_at: datetime = Field(default_factory=utc_now)
