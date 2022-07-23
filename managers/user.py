from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models import ClientModel


class ClientManager:
    @staticmethod
    def register(client_data):
        client_data["password"] = generate_password_hash(
            client_data["password"], method="sha256"
        )
        client = ClientModel(**client_data)
        try:
            db.session.add(client)
            return AuthManager.encode_token(client)
        except Exception as ex:
            raise BadRequest(str(ex))

    @staticmethod
    def login(data):
        try:
            client = ClientModel.query.filter_by(email=data["email"]).first()
            if client and check_password_hash(client.password, data["password"]):
                return AuthManager.encode_token(client)
            raise Exception
        except Exception:
            raise BadRequest("Invalid username or password")
