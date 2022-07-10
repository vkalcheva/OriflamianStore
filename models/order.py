from db import db


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
    status = db.Column(db.String(20), nullable=False)

    products = db.relationship("ProductModel", lazy="dynamic")

