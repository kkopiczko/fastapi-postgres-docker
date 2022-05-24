from fastapi import Depends
import database as _db
import models as _models
import schemas as _schemas
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def _create_database():
    """Creates tables according to the models"""
    return _db.Base.metadata.create_all(bind=_db.engine)

# function that creates database session
def get_db():
    db = _db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def create_contact(input_contact_data: _schemas.ContactCreate, db: "Session") -> _schemas.Contact:
    contact = _models.Contact(**input_contact_data.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return _schemas.Contact.from_orm(contact)

async def get_all_contacts(db: "Session") -> List[_schemas.Contact]:
    contacts = db.query(_models.Contact).all()
    return list(map(_schemas.Contact.from_orm, contacts))

async def get_contact_by_id(id: int, db: "Session") -> _schemas.Contact:
    contact = db.query(_models.Contact).filter(_models.Contact.id == id).first()
    return contact

async def delete_contact(contact: _models.Contact, db: "Session"):
    db.delete(contact)
    db.commit()