from pydantic import BaseModel

class ActorSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True