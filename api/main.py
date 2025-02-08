from fastapi import FastAPI, Depends, HTTPException
from authx import AuthX,RequestToken
from loader import  config
from passlib.context import CryptContext
from pydantic import BaseModel
app = FastAPI()


class UserCreate(BaseModel):
    username: str
    password: str

auth = AuthX(config=config)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
auth.handle_errors(app)

@app.post("/register")
def register(user: UserCreate):
     if user.username in user.password:
          raise HTTPException(status_code=400, detail="Username already registered")
     hashed_password = pwd_context.hash(user.password)

     return {"ok": True}

@app.post("/login")
def login(username: str, password: str):
     ...

