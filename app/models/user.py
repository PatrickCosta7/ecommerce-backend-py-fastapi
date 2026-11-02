from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional

from sqlalchemy import table
from sqlmodel import Field, Relationship, SQLModel


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    CUSTOMER = "CUSTOMER"
    DELIVERY = "DELIVERY"


class User(SQLModel, table=True):
    __tablename__ = "users"

    # id: int | None = Field(default=None, primary_key=True) -> modern Python syntax for optional fields
    id: Optional[int] = Field(default=None, primary_key=True)

    email: str = Field(index=True, unique=True)
    hashed_password: str = Field()
    name: str = Field(index=True)
    profile_picture: Optional[str] = None
    address: Optional[str] = None

    role: UserRole = Field(default=UserRole.CUSTOMER, index=True)

    active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    #One-to-many relationship
    orders: List["Order"] = Relationship(back_populates="user")
    reviews: List["Review"] = Relationship(back_populates="user")
    cart: Optional["Cart"] = Relationship(back_populates="user")





    
    