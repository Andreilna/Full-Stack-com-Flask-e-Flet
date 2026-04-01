from pydantic import BaseModel

class SeriesSchema(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True