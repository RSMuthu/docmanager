from sqlmodel import Field, SQLModel, Relationship
from .enum import DocType
from .base import IdMixin, TimestampMixin, SoftDeleteMixin, BaseModel


class DocBase(SQLModel):
    type: DocType = Field(..., description="Type of the document", nullable=False)
    title: str = Field(..., description="Title of the document", nullable=False)
    position: int = Field(..., description="position of the document", nullable=False, unique=True, index=True)  # indexed to help in ordering

class Doc(BaseModel, DocBase, IdMixin, TimestampMixin, SoftDeleteMixin, table=True):
    __tablename__ = "Docs"


    def __repr__(self):
        return f"<Doc ((id: {self.id}, title: {self.title}, type: {self.type})>"
