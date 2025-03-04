from dotenv import load_dotenv
from os import getenv as env
from authx import AuthXConfig
load_dotenv()
TOKEN = env("Token")

config = AuthXConfig(
     JWT_ALGORITHM = "HS256",
     JWT_SECRET_KEY = f"{env('SECRET_KEY')}",
     JWT_TOKEN_LOCATION = ["headers"],
)