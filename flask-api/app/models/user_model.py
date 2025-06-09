from app import db
import uuid
from sqlalchemy.dialects.postgresql import UUID

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    def __init__(self, name,email, password):
        self.name = name
        self.email = email
        self.password = password
        
    def serialize(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "email": self.email
        }
