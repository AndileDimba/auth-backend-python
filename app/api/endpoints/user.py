from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from app.domain.entities import UserUpdate
from app.domain.services import UserService
from app.api.dependencies import get_user_service
from app.core.config import settings

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return email
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.patch("/user/update")
def update_user(
    update_data: UserUpdate,
    user_email: str = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service)
):
    # In real implementation, get user ID from DB using email
    user = user_service.update_user(1, update_data)  # Replace with actual user ID lookup
    return user