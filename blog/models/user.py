from pydantic import BaseModel, EmailStr

# Input validation for creating users
class User(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True

# Response model (subset)
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True
