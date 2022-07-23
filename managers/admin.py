from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models import AdminModel


class AdminManager:
    @staticmethod
    def create_admin(admin_data):
        admin_data["password"] = generate_password_hash(admin_data["password"])
        admin = AdminModel(**admin_data)
        db.session.add(admin)
        db.session.commit()
        return AuthManager.encode_token(admin)

    @staticmethod
    def login_admin(data):
        try:
            admin = AdminModel.query.filter_by(email=data["email"]).first()
            if admin and check_password_hash(admin.password, data["password"]):
                return AuthManager.encode_token(admin)
            raise Exception
        except Exception:
            raise BadRequest("Invalid username or password")
