from db.database import get_db
from typing import List, Optional
from sqlalchemy.orm import Session
from models.post import Post, PostResponse
from db.models import Post as PostModel, PostCategory
from fastapi import APIRouter, Depends, HTTPException, Query, Response

router = APIRouter()

@router.get("/", response_model=List[PostResponse], summary="Get all posts")
def get_posts(
    category: Optional[PostCategory] = Query(None, description="Filter by category"),
    db: Session = Depends(get_db),
    response: Response = None,
):
    query = db.query(PostModel)
    if category:
        query = query.filter(PostModel.category == category)

    posts = query.all()
    if not posts:
        response.status_code = 204  # No Content
        return []

    return posts

@router.post("/", response_model=PostResponse, summary="Create a new post")
def create_post(post: Post, db: Session = Depends(get_db)):
    db_post = PostModel(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("/{post_id}", response_model=PostResponse, summary="Get a single post")
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(PostModel).filter(PostModel.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/{post_id}", response_model=PostResponse, summary="Replace a post")
def update_post(post_id: int, post: Post, db: Session = Depends(get_db)):
    db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    for key, value in post.dict().items():
        setattr(db_post, key, value)

    db.commit()
    db.refresh(db_post)
    return db_post

@router.patch("/{post_id}", response_model=PostResponse, summary="Update part of a post")
def partial_update_post(post_id: int, post: Post, db: Session = Depends(get_db)):
    db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    for key, value in post.dict(exclude_unset=True).items():
        setattr(db_post, key, value)

    db.commit()
    db.refresh(db_post)
    return db_post

@router.delete("/{post_id}", status_code=204, summary="Delete a post")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(PostModel).filter(PostModel.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    db.delete(post)
    db.commit()
    return {"message": "Post deleted successfully"}
