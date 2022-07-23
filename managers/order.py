from collections import Counter
from flask import request
from werkzeug.exceptions import BadRequest

from db import db
from models import ProductModel, OrderModel, ProductsInOrder, State


class OrderManager:
    @staticmethod
    def create(data, user):
        """
        Expect a token and a list of item ids from the request body.
        Construct an order and talk to the Strip API to make a charge.
        """
        data = request.get_json()
        data["client_id"] = user.id

        products = []
        product_id_quantities = Counter(data["product_ids"])

        for _id, count in product_id_quantities.most_common():
            product = ProductModel.query.filter_by(id=_id).first()
            if not product:
                return BadRequest

            products.append(ProductsInOrder(product_id=_id, quantity=count))

        order = OrderModel(products=products, client_id=user.id)

        db.session.add(order)
        return order

    @staticmethod
    def approve(order_id):
        OrderModel.query.filter_by(id=order_id).update({"status": State.approved})

    @staticmethod
    def reject(order_id):
        OrderModel.query.filter_by(id=order_id).update({"status": State.rejected})
