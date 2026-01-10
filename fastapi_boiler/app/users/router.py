# imports
from fastapi import APIRouter, Depends, status
from app.core.dependencies import get_Current_User
from app.core.schemas import UserResponse
from app.users.model import User as UserModel

# defining router
router = APIRouter()


# setting up routes
@router.get("/me", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def read_users_me(current_user: UserModel = Depends(get_Current_User)):
    """
    Retrieves the current authenticated user
    """

    return current_user
