from fastapi import Path, Query, Depends, APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

@movie_router.get('/movies', tags= ['movies'], response_model= List[Movie], status_code= 200, dependencies= [Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = session() #Abro sesion de base de datos
    result = MovieService(db).get_movies() #Obtengo todas las movies
    return JSONResponse(content= jsonable_encoder(result), status_code= 200) #Retorno todas las movies pasandola por json

@movie_router.get('/movies/{id}', tags= ['movies'], response_model= Movie, status_code= 200)
def get_movie(id: int = Path(ge = 1, le= 2000)) -> Movie:
    db = session() #Abro sesion de base de datos
    result = MovieService(db).get_movie(id= id) #Obtengo la movie por id
    if not result:
        return JSONResponse(content= {'message': 'Movie not found'}, status_code= 404)
    return JSONResponse(content= jsonable_encoder(result), status_code= 200)

@movie_router.get('/movies/', tags= ['movies'], response_model= List[Movie], status_code= 200)
def get_movies_by_category(category: str = Query(min_length= 5, max_length= 15)) -> List[Movie]:
    db = session() #Abro sesion de base de datos
    result =  MovieService(db).get_movies_by_category(category = category)#Obtengo todas las movies por categoria
    if not result:
        return JSONResponse(content= {'message': 'Category not found'}, status_code= 404)
    return JSONResponse(content= jsonable_encoder(result), status_code= 200)

@movie_router.post('/movies', tags= ['movies'], response_model= dict, status_code= 201)
def create_movie(movie: Movie) -> dict:
    db = session() #Abro sesion de base de datos
    MovieService(db).create_movie(movie) #Creo nueva movie con los parametros
    return JSONResponse(content= {'message': 'Movie created successfully'}, status_code= 201)

@movie_router.put('/movies/{id}', tags= ['movies'], response_model= dict, status_code= 200)
def update_movie(id: int, movie: Movie) -> dict:
    db = session() #Abro sesion de base de datos
    result = MovieService(db).get_movie(id= id) #Obtengo la movie por id
    if not result:
        return JSONResponse(content= {'message': 'Movie not found'}, status_code= 404)
    
    # Si existen, actualizo
    MovieService(db).update_movie(id= id, data= movie)
    return JSONResponse(content= {'message': 'Movie updated successfully'}, status_code= 200)

@movie_router.delete('/movies/{id}', tags= ['movies'], response_model= dict, status_code= 200)
def delete_movie(id: int) -> dict:
    db = session() #Abro sesion de base de datos
    result = MovieService(db).get_movie(id= id) #Obtengo la movie por id
    if not result:
        return JSONResponse(content= {'message': 'Movie not found'}, status_code= 404)
    
    MovieService(db).delete_movie(id = id)
    return JSONResponse(content= {'message': 'Movie deleted successfully'}, status_code= 200)