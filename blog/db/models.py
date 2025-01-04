from sqlalchemy import Column, Integer, String, Boolean, Enum
from db.database import Base
from enum import Enum as PyEnum

# Enum for post categories
class PostCategory(PyEnum):
    tech = "tech"
    lifestyle = "lifestyle"
    travel = "travel"

# Post model
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    author = Column(String)
    category = Column(Enum(PostCategory))
    is_published = Column(Boolean, default=False)

# User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
