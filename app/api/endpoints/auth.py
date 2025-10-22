from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from app.domain.services import AuthService
from app.api.dependencies import get_auth_service
from app.domain.entities import UserLogin, UserCreate
from app.core.security import create_access_token

router = APIRouter()

@router.post("/auth/register")
def register_user(
        user_data: UserCreate,
        auth_service: AuthService = Depends(get_auth_service) # This is not ideal, should be UserService
):
    # For simplicity, we'll use auth_service to access the user_repo directly
    # In a real app, this would typically go through a UserService
    try:
        user = auth_service.user_repo.create(user_data)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="User with this email already exists")
    return user


@router.post("/auth/login")
def login(
        user_data: UserLogin,
        auth_service: AuthService = Depends(get_auth_service)
):
    user = auth_service.authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}