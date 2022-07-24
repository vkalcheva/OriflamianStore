from datetime import datetime, timedelta

import jwt
from decouple import config
from flask_httpauth import HTTPTokenAuth
from jwt import ExpiredSignatureError, InvalidTokenError
from werkzeug.exceptions import BadRequest

from models import ClientModel, AdminModel


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {
            "sub": user.id,
            "exp": datetime.utcnow() + timedelta(days=2),
            "type": user.__class__.__name__,
        }
        return jwt.encode(payload, key=config("SECRET_KEY"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(
                jwt=token, key=config("SECRET_KEY"), algorithms=["HS256"]
            )
            return payload["sub"]
        except ExpiredSignatureError:
            raise BadRequest("Token expired!")
        except InvalidTokenError:
            raise BadRequest("Invalid token!")


auth = HTTPTokenAuth()


@auth.verify_token
def verify_token(token):
    user_id = AuthManager.decode_token(token)
    return AdminModel.query.filter_by(id=user_id).first()
