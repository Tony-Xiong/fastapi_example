

from fastapi import APIRouter
from pydantic.dataclasses import dataclass

router = APIRouter()

@router.get("/users")
async def get_user():
    return {"message": "Welcome to the user API!"}

@router.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    return {"message": f"Get user {user_id}!"}

@dataclass
class User:
    name: str
    email: str
    password: str