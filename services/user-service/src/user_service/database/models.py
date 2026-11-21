
from enum import StrEnum
from uuid import UUID

from sqlalchemy import Enum, String, Uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from uuid6 import uuid7


class Base(DeclarativeBase):
    pass


class UserRole(str, StrEnum):
    CUSTOMER = "customer"
    ADMIN = "admin"


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid7,
    )
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole),
        default=UserRole.CUSTOMER,
        nullable=False,
    )
