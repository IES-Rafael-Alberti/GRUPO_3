from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    token: str = None

class UserInDB(BaseModel):
    username: str
    hashed_password: str
