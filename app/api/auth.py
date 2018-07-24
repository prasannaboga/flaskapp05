from flask import g, jsonify, make_response
from flask_httpauth import HTTPBasicAuth
from mongoengine import DoesNotExist

from app.models.user import User

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(email_or_token, password):
    user = User.verify_auth_token(email_or_token)
    if not user:
        try:
            user = User.objects.get(email=email_or_token)
            if not user.verify_password(password):
                return False
        except DoesNotExist:
            return False
        g.user = user
    return True


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'errors': 'Unauthorized access'}), 401)
