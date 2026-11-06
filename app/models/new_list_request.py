from pydantic import BaseModel, Field


class NewListRequest(BaseModel):
    list_name: str = Field(min_length=1, max_length=100)

class ListResponse(BaseModel):
    list_id: int
    list_name: str

class ListsResponse(BaseModel):
    lists: list[ListResponse]
