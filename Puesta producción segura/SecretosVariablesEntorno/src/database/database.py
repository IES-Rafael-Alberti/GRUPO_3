import os
from datetime import timedelta
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from utils.utils import verify_password, get_password_hash, create_access_token
from models.User import User, UserInDB

# obtener las variables de entorno
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
MONGO_HOST = os.getenv("MONGO_HOST", "mongo")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_DB = os.getenv("MONGO_DB", "userdb")
MONGO_USER = os.getenv("MONGO_USER", "root")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "mi_contraseña_segura")
MONGO_AUTH_SOURCE = os.getenv("MONGO_AUTH_SOURCE", "admin")

class Database:
    def __init__(self):
        # construir la cadena de conexión con autenticación
        mongo_uri = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}?authSource={MONGO_AUTH_SOURCE}"
        self.client = AsyncIOMotorClient(mongo_uri)
        self.db = self.client[MONGO_DB]
        self.users_collection = self.db["users"]

    async def login(self, user: User):
        db_user = await self.users_collection.find_one({"username": user.username})
        if not db_user:
            raise HTTPException(status_code=400, detail="User not found")

        if not verify_password(user.password, db_user["hashed_password"]):
            raise HTTPException(status_code=400, detail="Incorrect password")

        access_token = create_access_token(
            data={"sub": user.username},
            expires_delta=timedelta(minutes=30)
        )
        return {"access_token": access_token, "token_type": "bearer"}

    async def create_user(self, user: User):
        existing_user = await self.users_collection.find_one({"username": user.username})
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already registered")

        hashed_password = get_password_hash(user.password)
        user_in_db = UserInDB(username=user.username, hashed_password=hashed_password)

        result = await self.users_collection.insert_one(user_in_db.dict())
        return {"id": str(result.inserted_id), "username": user.username}
