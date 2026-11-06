from fastapi import APIRouter, Depends, status

from app.dependencies import SessionDep
from app.models.new_list_request import ListResponse, ListsResponse, NewListRequest
from app.services.auth_services import get_current_user
from app.services.list_services import create_list_service, get_lists_service

router = APIRouter()

@router.get("/lists", response_model=ListsResponse)
async def get_lists(session: SessionDep, current_user = Depends(get_current_user)):
    return get_lists_service(session, current_user)

@router.post("/lists", response_model=ListResponse, status_code=status.HTTP_201_CREATED)
async def create_list(session: SessionDep, data: NewListRequest, current_user = Depends(get_current_user)):
    return create_list_service(session, data.list_name, current_user)