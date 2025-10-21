from sqlalchemy.orm import Session
from app.infrastructure.database import get_db
from app.domain.entities import UserInDB, UserCreate, UserUpdate
from app.infrastructure.models import User
from app.core.security import get_password_hash


class SQLUserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> UserInDB | None:
        user = self.db.query(User).filter(User.email == email).first()
        return UserInDB.from_orm(user) if user else None

    def create(self, user: UserCreate) -> UserInDB:
        hashed_password = get_password_hash(user.password)
        db_user = User(
            email=user.email,
            password=hashed_password,
            first_name=user.first_name,
            last_name=user.last_name
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return UserInDB.from_orm(db_user)

    def update(self, user_id: int, update_data: UserUpdate) -> UserInDB:
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError("User not found")

        for key, value in update_data.dict().items():
            setattr(user, key, value)

        self.db.commit()
        self.db.refresh(user)
        return UserInDB.from_orm(user)