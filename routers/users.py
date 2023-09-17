from fastapi import APIRouter
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.user import User

users_router = APIRouter()

@users_router.post('/login', tags= ['auth'], response_model= dict, status_code= 200)
def login(user: User) -> dict:
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(data= user.dict())
    return JSONResponse(content= {'message': 'Login successfully', 'token': token}, status_code= 200)