import datetime as _dt
from sqlalchemy import Column, DateTime, Integer, String
import database as _database

class Contact(_database.Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    phone_number = Column(String, index=True, unique=True)
    created_at = Column(DateTime, default=_dt.datetime.utcnow)