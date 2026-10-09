from fastapi import FastAPI

from app.database import engine, Base
from app.routers import auth, users, tasks


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="FastAPI CRUD Application",
    description="CRUD application with JWT authentication and PostgreSQL",
    version="1.0.0"
)


# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tasks.router)


@app.get("/")
def home():
    return {
        "message": "FastAPI CRUD Application is running"
    }