from app.models.user_model import User
from app import db
class UserService:
    def __init__(self):
        self.model=User
    
    def get_by_id(self,id:int):
        return self.model.query.get(id)
    
    def get_by_email(self,email:int):
        return self.model.query.filter_by(email=email).first()
    
    def get_all(self):
        return self.model.query.all()
    
    def create_user(self,name:str,email:str,password:str):
        user=User(name=name,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        return user