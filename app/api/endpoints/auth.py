from fastapi import APIRouter, Depends, HTTPException
from app.domain.services import AuthService
from app.api.dependencies import get_auth_service
from app.domain.entities import UserCreate
from app.core.security import create_access_token

router = APIRouter()


@router.post("/auth/login")
def login(
        user_data: UserCreate,
        auth_service: AuthService = Depends(get_auth_service)
):
    user = auth_service.authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}