from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    age: int
    email: EmailStr

user = User(name="AM",age=31, email="am@example.com")

print(user)
invalid_user = User(name="Jane Doe", age="thirty", email="jane.doe.com")
