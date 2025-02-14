from fastapi import APIRouter, HTTPException, Depends, status
from models.User import User
from typing import List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from utils.utils import create_access_token
from datetime import timedelta
from database.database import Database  

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
db = Database()

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = User(username=form_data.username, password=form_data.password)
    return await db.login(user)

@router.post("/register")
async def register(user: User):
    return await db.create_user(user)

@router.get("/users")
async def get_users(token: str = Depends(oauth2_scheme)):
    if not token or token == "undefined":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is missing or invalid"
        )

    users = await db.get_all_users()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authorized"
        )
    return users
