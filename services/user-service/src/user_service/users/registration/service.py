from sqlalchemy.orm import Session

from user_service.core.security import hash_password
from user_service.users.registration.repository import UserRepository


class UserService:

    def __init__(self, session: Session):
        self.session = session
        self.repository = UserRepository(session)

    def register_user(self, email: str, password: str):
        existing_user = self.repository.get_by_email(email)

        if existing_user:
            raise ValueError("Email is already registered")

        hashed_password = hash_password(password)

        try:
            user = self.repository.create(
                email=email,
                hashed_password=hashed_password,
            )

            self.session.commit()
            self.session.refresh(user)

            return user

        except Exception:
            self.session.rollback()
            raise