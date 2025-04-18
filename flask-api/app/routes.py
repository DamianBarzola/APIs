from flask import Blueprint

api = Blueprint('api', __name__)

from app.controllers.user_controller import users
from app.controllers.auth_controller import auth

api.register_blueprint(users, url_prefix='/users')
api.register_blueprint(auth, url_prefix='/auth')