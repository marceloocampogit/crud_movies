from config.database import base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float

class Movie(base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)