import datetime
from typing import Optional

from fastapi_users import schemas, models
from pydantic import BaseModel, EmailStr, ConfigDict, Field

from app.auth.database import Role


class UserRead(schemas.BaseUser[int]):
    id: models.ID
    fullName: str
    email: EmailStr
    imageUrl: Optional[str] = None
    role: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    created_at: datetime.datetime = Field(..., description="The time the product was created")
    updated_at: datetime.datetime = Field(..., description="The time the product was updated")

    model_config = ConfigDict(from_attributes=True)


class UserCreate(schemas.BaseUserCreate):
    fullName: str
    email: EmailStr
    password: str
    role: Role
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    fullName: Optional[str] = None
    role: Optional[Role] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None


class UserImage(BaseModel):
    id: int
    user_id: int


class UserImageCreate(BaseModel):
    user_id: int


class UserImageResponse(BaseModel):
    id: int
    user_id: int
    imageUrl: str

    class Config:
        from_attributes = True


# class UserAdminUpdate(BaseModel):
#     email: Optional[EmailStr] = None
#     is_active: Optional[bool] = None
#     is_superuser: Optional[bool] = None
#     is_verified: Optional[bool] = None
