from flask import Blueprint, jsonify

users=Blueprint('user', __name__)

from app.services.user_service import UserService

@users.route('/',methods=['GET'])
def get_users():
    users=UserService().get_all()
    serialized_users=[user.serialize() for user in users]
    return jsonify(serialized_users),200

@users.route('/<int:id>',methods=['GET'])
def get_user(id:int):
    return UserService().get_by_id(id)