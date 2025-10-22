from sqlalchemy import Column, BigInteger, String, TIMESTAMP
from sqlalchemy.sql import func
from .database import Base  # Base is defined in database.py

class User(Base):
    __tablename__ = "user"  # match the actual table name in your DB

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    name = Column(String(50))
    username = Column(String(50))
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())