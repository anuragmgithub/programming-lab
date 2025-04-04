from pydantic import BaseModel, ValidationError, field_validator

class User(BaseModel):
    username: str
    password: str
    age: int
    @field_validator('password')
    def password_must_contain_number(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain a number')
        return v
    

# Validate incoming user_data
user_data = {'username': 'Apptension', 'password': 'password1', 'age': 25}
user = User(**user_data)

assert user.username == 'password2'