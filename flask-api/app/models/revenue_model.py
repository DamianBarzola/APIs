from app import db 

class Revenue(db.Model):
    __tablename__ = 'revenue'
    
    month = db.Column(db.String(4),primary_key=True, unique=True, nullable=False,)
    revenue = db.Column(db.Integer, nullable=False)
    def __init__(self, month, revenue):
        self.month = month
        self.revenue = revenue
    def serialize(self):
        return {
            "month": self.month,
            "revenue": self.revenue
        }