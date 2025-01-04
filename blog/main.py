import os
from fastapi import FastAPI
from routes import posts, users
from db.database import engine, Base
from prometheus_fastapi_instrumentator import Instrumentator

# Initialize the database tables
Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI(
    title="Blog API",
    description="A blog API with database connection",
    version="1.0.0",
)
# Initialize the Instrumentator for Prometheus metrics
Instrumentator().instrument(app).expose(app)

# Include routers
app.include_router(posts.router, prefix="/posts", tags=["Posts"])
app.include_router(users.router, prefix="/users", tags=["Users"])


