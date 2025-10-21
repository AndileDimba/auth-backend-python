from abc import ABC, abstractmethod
from app.domain.entities import UserInDB, UserCreate, UserUpdate


class IUserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> UserInDB | None:
        pass

    @abstractmethod
    def create(self, user: UserCreate) -> UserInDB:
        pass

    @abstractmethod
    def update(self, user_id: int, update_data: UserUpdate) -> UserInDB:
        pass