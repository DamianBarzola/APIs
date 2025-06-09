from app import db
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Invoice(db.Model):
    __tablename__ = 'invoices'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True,nullable=False, default=uuid.uuid4)
    # customer_id = db.Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    customer_id = db.Column(UUID(as_uuid=True), db.ForeignKey('customers.id'), nullable=False)
    

    amount = db.Column(db.Integer,  nullable=False)
    status = db.Column(db.String(255),  nullable=False)
    date = db.Column(db.Date, nullable=False)
    
    def __init__(self, customer_id, amount, status, date):
        self.customer_id = customer_id
        self.amount = amount
        self.status = status
        self.date = date
        
    def serialize(self):
        return {
            "id": str(self.id),
            # "customer_id": str(self.customer_id),
            "amount": self.amount,
            "status": self.status,
            "date": self.date.isoformat(),
            "customer": {
                "id": str(self.customer_id),
                "name": self.customer.name,
                "email": self.customer.email,              
            }

        }
