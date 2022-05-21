from pydantic import BaseModel
from datetime import datetime

class _ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str

class Contact(_ContactBase):
    id: int
    created_at: datetime

class ContactCreate(_ContactBase):
    pass
