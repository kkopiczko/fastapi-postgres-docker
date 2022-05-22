import database as _db
import models as _models
from schemas import ContactCreate
from typing import TYPE_CHECKING

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