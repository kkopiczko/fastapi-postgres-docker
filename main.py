from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from typing import TYPE_CHECKING, List
from schemas import Contact, ContactCreate
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/api/contacts/", response_model=Contact)
async def create_contact(contact: ContactCreate, db: Session=Depends(_services.get_db)):
    return await _services.create_contact(input_contact_data=contact, db=db)

@app.get("/api/contacts/", response_model=List[Contact])
async def get_contacts(db: Session=Depends(_services.get_db)):
    return await _services.get_all_contacts(db=db)

@app.get("/api/contacts/{id}", response_model=Contact)
async def get_contact(id: int, db: Session=Depends(_services.get_db)):
    contact = await _services.get_contact_by_id(id=id, db=db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'A contact with id: {id} was not found')
    return contact

@app.delete("/api/contacts/{id}")
async def delete_contact(id: int, db: Session=Depends(_services.get_db)):
    contact = await _services.get_contact_by_id(id=id, db=db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'A contact with id: {id} was not found')
    await _services.delete_contact(contact=contact, db=db)
    return "Successfully deleted contact"

@app.put("/api/contacts/{id}", response_model=Contact)
async def update_contact(id: int, contact_data: ContactCreate, db: Session=Depends(_services.get_db)):
    contact = await _services.get_contact_by_id(id=id, db=db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'A contact with id: {id} was not found')
    updated_contact = await _services.update_contact(contact_data=contact_data, contact=contact, db=db)
    return updated_contact