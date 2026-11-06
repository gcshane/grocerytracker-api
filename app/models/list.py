from pydantic import BaseModel


class List(BaseModel):
    list_name : str

class NewListRequest(BaseModel):
    list_name: str