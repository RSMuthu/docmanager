from uuid import UUID
from sqlmodel import col, select, func
from api.models.doc import Doc
from api.interfaces.doc import DocRead, DocCreate, DocUpdate
from api.utils.exceptions import NotFoundError, DuplicateConstraint
from api.interfaces.utils import List
from .base import BaseService


class DocService(BaseService):

    async def get_doc(self, doc_id: UUID) -> DocRead:
        """
        Fetches an Doc Entry by its unique identifier.

        Args:
            doc_id (UUID): The unique identifier of the Doc entry.

        Raises:
            NotFoundError: If no Doc is found with the provided identifier

        Returns:
            DocRead: The Doc object
        """
        # pylint: disable=invalid-unary-operand-type
        doc = (
            await Doc.get(db=self.db, filters=[Doc.id == doc_id, ~col(Doc.is_deleted)])
        ).one_or_none()
        if doc is None:
            raise NotFoundError("Doc entry not found")
        return doc

    async def get_docs(self) -> List[DocRead]:
        """
        Retrieve a list of Doc entries

        Returns:
            List[DocRead]: A list of Doc entries.
        """
        # pylint: disable=invalid-unary-operand-type
        res = await Doc.get(db=self.db, filters=[~col(Doc.is_deleted)])
        return {"data": res.all()}

    async def create_doc(self, data: DocCreate) -> DocRead:
        """
        Creates a new Doc entry with the provided data.

        Args:
            data (DocCreate): An object containing the details required to create a new Doc entry.
        """
        exist_doc = (await Doc.get(db=self.db, filters=[Doc.position == data.position, ~col(Doc.is_deleted)])).one_or_none()
        if exist_doc:
            raise DuplicateConstraint("Position is already taken")
        if data.position is None:
            max_position = (await self.db.execute(select(func.max(Doc.position)).where(~col(Doc.is_deleted)))).scalar()
            print ("max", max_position)
            data.position = (-1 if max_position is None else max_position) + 1  # to start count from zero
        print (data.model_dump())
        new_doc = Doc(**data.model_dump())
        await new_doc.save(self.db)
        return new_doc

    async def delete_doc(self, doc_id: UUID):
        """
        Deletes the Doc entry identified by doc_id.

        Args:
            doc_id (UUID): The ID of the Doc entry to be deleted.

        Raises:
            NotFoundError: If the Doc entry is not found.
        """
        doc = await self.get_doc(doc_id)
        await doc.delete(self.db)

    async def update_doc(self, doc_id: UUID, data: DocUpdate) -> DocRead:
        """
        Updates the Doc Entry identified by doc_id with the provided data.

        Args:
            doc_id (UUID): The ID of the Doc entry to be updated.
            data (DocUpdate): An object containing the details to update the Doc entry.

        Returns:
            DocRead: The updated Doc object.

        Raises:
            NotFoundError: If the Doc is not found.
        """
        existing_doc = (await Doc.get(db=self.db, filters=[Doc.position == data.position, ~col(Doc.is_deleted)])).one_or_none()
        if existing_doc.id == doc_id:
            raise DuplicateConstraint("Doc cannot have same position as another")
        doc = await self.get_doc(doc_id)
        await doc.update(self.db, data)
        return doc
