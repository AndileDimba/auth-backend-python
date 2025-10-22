from app.domain.repositories import IUserRepository
from app.domain.entities import UserCreate, UserInDB, UserUpdate, UserInDBWithPassword
from app.core.security import verify_password, get_password_hash


class AuthService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def authenticate_user(self, email: str, password: str) -> UserInDBWithPassword | None:
        user = self.user_repo.get_by_email(email)
        if not user or not verify_password(password, user.password):
            return None
        return user


class UserService:
    def __init__(self, user_repo: IUserRepository):
        self.user_repo = user_repo

    def get_user_by_email(self, email: str) -> UserInDB | None:
        return self.user_repo.get_by_email(email)

    def update_user(self, user_id: int, update_data: UserUpdate) -> UserInDB:
        return self.user_repo.update(user_id, update_data)