from db import db
from models.enums import RoleType


class BaseUserModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)


class PartnerModel(BaseUserModel):
    __tablename__ = "partners"

    role = db.Column(
        db.Enum(RoleType),
        default=RoleType.partner,
        nullable=False
    )


class ClientModel(BaseUserModel):
    __tablename__ = "clients"

    orders = db.relationship("OrderModel", backref="order", lazy="dynamic")
    role = db.Column(
        db.Enum(RoleType),
        default=RoleType.client,
        nullable=False
    )


class AdminModel(BaseUserModel):
    __tablename__ = 'admins'

    role =db.Column(
        db.Enum(RoleType),
        default=RoleType.admin,
        nullable=False
    )

    products = db.relationship("ProductModel", backref="product", lazy="dynamic")
    categories = db.relationship("CategoryModel", backref="category", lazy="dynamic")














