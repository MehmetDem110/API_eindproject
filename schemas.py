from pydantic import BaseModel

class SnackBase(BaseModel):
    name: str
    description: str

class SnackCreate(SnackBase):
    pass

class SnackUpdate(SnackBase):
    pass

class Snack(SnackBase):
    id: int

    class Config:
        orm_mode = True
