from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    email: str
    name: str
    username: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: str
    username: str

class UserResponse(UserBase):
    id: int
    updated_at: datetime

    model_config = {"from_attributes": True}