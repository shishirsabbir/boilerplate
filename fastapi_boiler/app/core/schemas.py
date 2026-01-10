# imports
from pydantic import BaseModel, EmailStr
from datetime import datetime


# defining user body
class User(BaseModel):
    first_name: str
    last_name: str
    user_name: str
    email: EmailStr
    password: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "kuddus",
                    "last_name": "ali",
                    "user_name": "kuddusali",
                    "email": "kuddusali@mail.com",
                    "password": "test1234",
                },
                {
                    "first_name": "sokina",
                    "last_name": "begum",
                    "user_name": "sokinabegum",
                    "email": "sokinabegum@mail.com",
                    "password": "test1234",
                },
            ]
        }
    }


# defining a user response body class
class UserResponse(BaseModel):
    id: str
    first_name: str
    last_name: str
    user_name: str
    email: str
    # password: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}  # for pydantic v2


# defining login class
class Login(BaseModel):
    email: EmailStr
    password: str


# schema for token response
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# schema for token data
class TokenData(BaseModel):
    user_id: str | None = None
