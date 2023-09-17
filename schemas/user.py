from pydantic import BaseModel, Field

class User(BaseModel):
    email: str = Field(default= "admin@gmail.com",min_length= 5, max_length= 50)
    password: str = Field(default= "admin",min_length= 4, max_length= 50)