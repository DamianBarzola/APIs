from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app import bcrypt
from datetime import datetime
import os
import jwt

auth=Blueprint('auth', __name__)

@auth.route('/login',methods=['POST'])
def login():    
    data=request.get_json()
    if not data:
        return jsonify({"message":"Missing fields"}),400
    email=data.get("email")
    password=data.get("password")
    if not email or not password:
        return jsonify({"message":"Missing fields"}),400
    user=UserService().get_by_email(email=email)
    if not user:
        return jsonify({"message":"User not found"}),404  
    if not bcrypt.check_password_hash(user.password,password):
        return jsonify({"message":"Invalid credentials"}),401   
    payload={
        "name":user.name,
        "email":user.email,
        "id":str(user.id),
        "iat": datetime.utcnow(),
    } 
    token =jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm='HS256')
    return jsonify({"token":token}),200
    
@auth.route('/register',methods=['POST'])
def register():
    data=request.get_json()
    if not data:
        return jsonify({"message":"Missing fields"}),400
    name=data.get('name')
    email=data.get('email')
    password=data.get('password')
    if not name or not email or not password:
        return jsonify({"message":"Missing fields"}),400
    if UserService().get_by_email(email):
        return jsonify({"message":"User already exists"}),400
    hashed_pass=bcrypt.generate_password_hash(password).decode('utf-8')
    UserService().create_user(name,email,hashed_pass)
    return jsonify({"message":"User created successfully"}),201

@auth.route('/logout',methods=['POST'])
def logout():
    pass

@auth.route('/me',methods=['GET'])
def user():
    pass
