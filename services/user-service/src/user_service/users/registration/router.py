from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from user_service.database.session import get_db
from user_service.users.registration.schemas import UserCreate, UserResponse
from user_service.users.registration.service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    user_service = UserService(db)

    try:
        user = user_service.register_user(
            email=user_data.email,
            password=user_data.password,
        )

        return user

    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error