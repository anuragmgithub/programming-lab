from pydantic import BaseModel, Field, ValidationError

class User(BaseModel):
    name: str
    age: int = Field(...,ge=18,le=100)

try:
    user = User(name="john", age=150)
except ValidationError as e:
    print(e)
