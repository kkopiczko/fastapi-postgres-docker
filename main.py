from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from typing import TYPE_CHECKING, List
from schemas import Contact, ContactCreate
import services as _services


app = FastAPI()

@app.post("/api/contacts/", response_model=Contact)
async def create_contact(contact: ContactCreate, db: Session=Depends(_services.get_db)):
    return await _services.create_contact(input_contact_data=contact, db=db)