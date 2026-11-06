from pydantic import BaseModel, EmailStr, Field


class Token(BaseModel):
    access_token: str
    token_type: str

class SignUpRequest(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8)
    email: EmailStr
    name: str = Field(min_length=1, max_length=100)
    alert: bool