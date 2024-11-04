# FIXME: Buggy code -- Do not use this

from uuid import UUID
from fastapi import APIRouter, Depends, status
from api.services import DocService
from api.interfaces.utils import List
from api.interfaces import DocRead, DocCreate, DocUpdate

doc_router = APIRouter(prefix="/docs")


@doc_router.get("/{doc_id}", response_model=DocRead)
async def get_doc(doc_id: UUID, service: DocService = Depends(DocService)):
    """
    Endpoint to get a Doc entry details
    """
    return await service.get_doc(doc_id)


@doc_router.get("", response_model=List[DocRead])
async def get_docs(service: DocService = Depends(DocService)):
    """
    Endpoint to get a list of Doc entries
    """
    return await service.get_docs()


@doc_router.post("", status_code=status.HTTP_201_CREATED, response_model=DocRead)
async def create_doc(info: DocCreate, service: DocService = Depends(DocService)):
    """
    Endpoint to create a Document entry
    """
    return await service.create_doc(info)


@doc_router.delete("/{doc_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_doc(doc_id: UUID, service: DocService = Depends(DocService)):
    """
    Endpoint to delete a Doc entry
    """
    await service.delete_doc(doc_id)


@doc_router.patch("/{doc_id}", response_model=DocRead)
async def update_doc(doc_id: UUID, info: DocUpdate, service: DocService = Depends()):
    """
    Endpoint to update the details of the doc entry
    """
    return await service.update_doc(doc_id, info)
