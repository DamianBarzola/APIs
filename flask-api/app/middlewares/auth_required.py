
from flask import request, jsonify, g
from functools import wraps
import jwt
import os

def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Missing token'}), 401
        try:
            user=jwt.decode(token.split(" ")[1], os.getenv('SECRET_KEY'), algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
        g.user = user
        return f(*args, **kwargs)
    return decorated_function