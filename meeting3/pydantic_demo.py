from pydantic import BaseModel

class A:
    pass

class Fruit(BaseModel):
    name: str
    a: A
