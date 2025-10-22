from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    email: str
    name: Optional[str] = None
    username: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None

class UserLogin(BaseModel):
    email: str
    password: str

class UserInDBBase(UserBase):
    id: int
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}

class UserInDB(UserInDBBase):
    pass

class UserInDBWithPassword(UserInDBBase):
    password: str

