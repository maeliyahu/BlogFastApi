from pydantic import BaseModel
from enum import Enum
from typing import Optional

# Enum for post categories
class PostCategory(str, Enum):
    tech = "tech"
    lifestyle = "lifestyle"
    travel = "travel"

# Input validation for creating posts
class Post(BaseModel):
    title: str
    content: str
    author: str
    category: PostCategory
    is_published: Optional[bool] = False

# Response model (subset)
class PostResponse(BaseModel):
    id: int
    title: str
    author: str
    category: PostCategory

    class Config:
        from_attributes = True