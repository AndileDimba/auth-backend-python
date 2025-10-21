from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    first_name: str
    last_name: str

class UserInDB(UserBase):
    id: int
    updated_at: datetime

    class Config:
        orm_mode = True