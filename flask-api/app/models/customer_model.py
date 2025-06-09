from app import db
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True,nullable=False, default=uuid.uuid4)
    name = db.Column(db.String(255),  nullable=False)
    email = db.Column(db.String(255),  nullable=False)
    image_url = db.Column(db.String(255),  nullable=False)
    invoices = db.relationship('Invoice', backref='customer', lazy=True)
    

    def __init__(self, name, email, image_url):
        self.name = name
        self.email = email
        self.image_url = image_url
        
        
        
    def serialize(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "email": self.email,
            "image_url": self.image_url,
             "invoices": [{"id": str(invoice.id), 
                           "amount": invoice.amount,
                           "status": invoice.status,
                           "date": invoice.date.isoformat()
                           } for invoice in self.invoices] 
        }
