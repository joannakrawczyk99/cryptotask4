from pydantic import BaseModel

class Key(BaseModel):
    value: str
    public_key: str
    private_key: str

