from pydantic import BaseModel


class Message(BaseModel):
    value: str
