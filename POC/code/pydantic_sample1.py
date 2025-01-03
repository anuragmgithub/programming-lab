from pydantic import BaseModel, validator

class User(BaseModel):
    name: str
    email: str

    @validator("name", pre=True, always=True)
    def capitalize_name(cls, value):
        return value.title()

user = User(name="john doe", email="john.doe@example.com")
print(user)
