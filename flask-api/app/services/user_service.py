from app.models.user_model import User
from app import db
class UserService:
    def __init__(self):
        self.model=User
    
    def get_by_id(self,id:str):
        return self.model.query.get(id)
    
    def get_by_email(self,email:str):
        return self.model.query.filter_by(email=email).first()
    
    def get_all(self):
        return self.model.query.all()
    
    def create_user(self,name:str,email:str,password:str):
        user=User(name=name,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        return user
    
    def delete_user(self,id:str):
        user=self.model.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return user
    
    def update_user(self,id:str,name:str,email:str,password:str):
        user=self.model.query.get(id)
        user.name=name
        user.email=email
        user.password=password
        db.session.commit()
        return user
    
    