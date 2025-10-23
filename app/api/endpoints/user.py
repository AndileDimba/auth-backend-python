from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from app.domain.entities import UserUpdate
from app.domain.services import UserService
from app.api.dependencies import get_user_service
from app.core.config import settings

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    user_service: UserService = Depends(get_user_service),
):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = user_service.get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.patch("/user/update")
def update_user(
    update_data: UserUpdate,
    user_email: str = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service)
):

    user_db = user_service.get_user_by_email(user_email)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    user = user_service.update_user(user_db.id, update_data)
    return user

@router.get("/me")
async def read_current_user(current_user=Depends(get_current_user)):
    return {
        "email": current_user.email,
        "name": current_user.name,
        "username": current_user.username,
    }