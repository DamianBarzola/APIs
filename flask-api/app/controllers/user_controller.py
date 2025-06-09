from flask import Blueprint, jsonify

users=Blueprint('user', __name__)

from app.services.user_service import UserService

@users.route('/',methods=['GET'])
def get_users():
    users=UserService().get_all()
    serialized_users=[user.serialize() for user in users]
    return jsonify(serialized_users),200

@users.route('/<id>',methods=['GET'])
def get_user(id:str):

    user=UserService().get_by_id(id)
    if user:
        return jsonify(user.serialize()),200
    else:
        return jsonify({"message":"User not found"}),404
    
@users.route('/',methods=['POST'])
def create_user():
    data=request.json
    user=UserService().create_user(data['name'],data['email'],data['password'])
    return jsonify(user.serialize()),201