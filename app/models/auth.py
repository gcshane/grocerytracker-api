from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class SignUpRequest(BaseModel):
    username: str
    password: str
    email: str
    name: str
    alert: bool