# imports
from sqlalchemy.orm import Session
from sqlalchemy import select, insert
from app.users.model import User as UserModel
from app.core.security import hash_Password, verify_Password
from app.core.schemas import User


# db service functions
def create_New_User(db: Session, user_data: User) -> UserModel:
    """
    Creates a new user in database
    """

    # hash password before storing to db
    password_hash = hash_Password(user_data.password)

    user_dict = {
        "first_name": user_data.first_name,
        "last_name": user_data.last_name,
        "user_name": user_data.user_name,
        "email": user_data.email,
        "password": password_hash,
    }

    user_data_db = db.scalars(insert(UserModel).returning(UserModel), [user_dict]).one()

    db.commit()
    db.refresh(user_data_db)

    return user_data_db


def get_User_by_Username(db: Session, user_name: str) -> UserModel | None:
    """
    Retrieves user by username
    """

    return db.scalar(select(UserModel).filter(UserModel.user_name == user_name))


def get_User_by_Email(db: Session, email: str) -> UserModel | None:
    """
    Retrieves user by email
    """

    return db.scalar(select(UserModel).filter(UserModel.email == email))


# authenticate user function (service function)
def authenticate_User(db: Session, username: str, password: str) -> UserModel | None:
    """
    Authenticate a user by username and password
    """

    user = get_User_by_Username(db, user_name=username)

    if not user:
        return None
    if not verify_Password(password, user.password):
        return None

    # if everything is okay
    return user
