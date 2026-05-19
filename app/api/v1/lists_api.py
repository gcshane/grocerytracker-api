from fastapi import APIRouter, Depends
from app.services.auth_services import get_current_user
from app.services.list_services import create_list_service, get_lists_service
from app.models.new_list_request import NewListRequest
from app.dependencies import SessionDep

router = APIRouter()

@router.get("/lists")
async def get_lists(session: SessionDep, current_user = Depends(get_current_user)):
    return get_lists_service(session, current_user)

@router.post("/lists")
async def create_list(session: SessionDep, data: NewListRequest, current_user = Depends(get_current_user)):
    return create_list_service(session, data.list_name, current_user)