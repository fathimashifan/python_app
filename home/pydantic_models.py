from pydantic import BaseModel, Field
from typing import Optional

class MovieDisplayModel(BaseModel):
    display_id: Optional[int] = Field(None, alias='display_id')
    movie_name: Optional[str] = Field(None, max_length=25)
    image: str

    class Config:
        orm_mode = True
class MovieDisplayCreateModel(BaseModel):
    movie_name: str = Field(max_length=25)
    image: str

    class Config:
        orm_mode = True
