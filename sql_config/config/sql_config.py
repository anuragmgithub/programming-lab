from pydantic import BaseModel, Field, validator 
from typing import Optional

class SQLConfig(BaseModel):
    host: str = Field(..., description="Database host address")
    port: int = Field(..., description="Database port number")
    user: str = Field(..., description="Database username")
    password: str = Field(..., description="Database password")
    database: str = Field(..., description="Database name")

    @validator('host')
    def validate_host(cls, v):
        if not v:
            raise ValueError("Host cannot be empty")
        return v
    
    @validator('port')
    def validate_port(cls, v):
        if not (0 < v < 65536):
            raise ValueError("Port must be between 1 and 65535")
        return v
    
    @validator('user')
    def validate_user(cls, v):
        if not v:
            raise ValueError("User cannot be empty")
        return v
    
    @validator('password')
    def validate_password(cls, v):
        if not v:
            raise ValueError("Password cannot be empty")
        return v
    
    @validator('database')
    def validate_database(cls, v):
        if not v:
            raise ValueError("Database cannot be empty")
        return v
