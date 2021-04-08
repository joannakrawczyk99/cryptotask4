from pydantic import BaseModel

class Key(BaseModel):
    value: str
    private_key: str
    public_key: str
