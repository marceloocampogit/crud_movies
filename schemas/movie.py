from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length= 5, max_length= 15)
    overview: str = Field(min_length= 15, max_length= 50)
    year: int = Field(le= 2022)
    category: str = Field(min_length= 5, max_length= 15)
    rating: float = Field(gt= 1, le= 10)

    # Crear configuracion inicial para la documentacion
    class Config:
        json_schema_extra = {
            "example": 
            {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripcion",
                "year": 2022,
                "category": "Acción",
                "rating": 7.8
            }
        }