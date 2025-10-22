from fastapi import Depends
from app.infrastructure.database import get_db
from app.infrastructure.repositories.user_repository import SQLUserRepository
from app.domain.services import AuthService, UserService

def get_user_repository():
    db = next(get_db())
    try:
        yield SQLUserRepository(db)
    finally:
        db.close()

def get_auth_service(user_repo: SQLUserRepository = Depends(get_user_repository)):
    return AuthService(user_repo)

def get_user_service(user_repo: SQLUserRepository = Depends(get_user_repository)):
    return UserService(user_repo)