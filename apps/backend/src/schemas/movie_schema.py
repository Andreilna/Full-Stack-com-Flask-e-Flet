from pydantic import BaseModel

class MovieSchema(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True