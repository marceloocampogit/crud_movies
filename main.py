from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security.http import HTTPAuthorizationCredentials
from utils.jwt_manager import create_token
from config.database import base, engine
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.users import users_router

app = FastAPI() 
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(users_router)

base.metadata.create_all(bind = engine)

@app.get('/', tags= ['home'])
def message():
    return HTMLResponse('<h1>Por suerte es viernes, bro</h1>')