from models.movie import Movie as MovieModel
from schemas.movie import Movie

class MovieService():

    def __init__(self, db):
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def get_movie(self, id: int):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    
    def get_movies_by_category(self, category: str):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result
    
    def create_movie(self, movie: Movie):
        movie = MovieModel(**movie.dict())
        self.db.add(movie)
        self.db.commit()
        return
    
    def update_movie(self, id: int, data: Movie):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.category = data.category
        movie.rating = data.rating
        self.db.commit()
        return
    
    def delete_movie(self, id: int):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).delete()
        self.db.commit()
        return