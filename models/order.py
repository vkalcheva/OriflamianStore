from sqlalchemy import func

from db import db
from models.enums import State


class ProductsInOrder(db.Model):
    __tablename__ = "products_in_order"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    quantity = db.Column(db.Integer)

    product = db.relationship("ProductModel")
    order = db.relationship("OrderModel", back_populates="products")


class OrderModel(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    create_on = db.Column(db.DateTime, server_default=func.now())
    status = db.Column(db.Enum(State), default=State.pending, nullable=False)

    client_id = db.Column(db.Integer, db.ForeignKey("clients.id"))
    client = db.relationship("ClientModel")
    products = db.relationship("ProductsInOrder", back_populates="order")
