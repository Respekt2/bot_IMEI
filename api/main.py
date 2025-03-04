from fastapi import FastAPI, HTTPException
from authx import AuthX
from bot_IMEI.loader import config
from passlib.context import CryptContext
from pydantic import BaseModel
import uvicorn
app = FastAPI()


class UserCreate(BaseModel):
    username: str
    password: str

auth = AuthX(config=config)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
auth.handle_errors(app)

@app.post("/register")
async def register(user: UserCreate):
     if user.username in user.password:
          raise HTTPException(status_code=400, detail="Username already registered")
     hashed_password = pwd_context.hash(user.password)

     return {"ok": True}

@app.post("/login")
async def login(username: str, password: str):
     ...

if __name__ =="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)