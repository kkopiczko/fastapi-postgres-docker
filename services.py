import database as _db
import models as _models

def _create_database():
    """Creates tables according to the models"""
    return _db.Base.metadata.create_all(bind=_db.engine)