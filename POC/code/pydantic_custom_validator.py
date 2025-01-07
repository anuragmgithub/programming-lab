from pydantic import BaseModel, validator, ValidationError

class User(BaseModel):
    name: str
    email: str

    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email address')
        return v

# Invalid email address
try:
    user = User(name="John", email="invalid-email")
except ValidationError as e:
    print(e)
