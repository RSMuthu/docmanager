from typing import Optional
from pydantic import ConfigDict
from sqlmodel import SQLModel
from api.models import IdMixin, TimestampMixin
from api.models.doc import DocBase
from api.models.enum import DocType


class DocCreate(DocBase):
    model_config = ConfigDict(extra="forbid")


class DocRead(DocBase, IdMixin, TimestampMixin):
    pass


class DocUpdate(SQLModel):
    type: Optional[DocType] = None
    title: Optional[str] = None
    position: Optional[int] = None

    model_config = ConfigDict(extra="forbid")
