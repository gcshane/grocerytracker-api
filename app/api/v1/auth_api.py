from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.dependencies import SessionDep
from app.services.auth_services import login_service, signup_service
from app.models.auth import SignUpRequest

router = APIRouter()

@router.post("/auth/login")
async def login(session: SessionDep, form_data: OAuth2PasswordRequestForm = Depends()):
    return login_service(session, form_data)

@router.post("/auth/signup")
async def signup(session: SessionDep, data: SignUpRequest):
    return signup_service(session, data)