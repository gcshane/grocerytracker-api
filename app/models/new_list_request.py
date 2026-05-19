from pydantic import BaseModel

class NewListRequest(BaseModel):
    list_name: str
