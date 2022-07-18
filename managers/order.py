from collections import Counter
from flask import request
from werkzeug.exceptions import BadRequest

from db import db
from models import ProductModel, OrderModel, ProductsInOrder


class OrderManager:
    @staticmethod
    def create(data, client):
        """
        Expect a token and a list of item ids from the request body.
        Construct an order and talk to the Strip API to make a charge.
        """
        data["client_id"] = client.id
        data = request.get_json()
        products = []
        product_id_quantities = Counter(data["product_ids"])

        for _id, count in product_id_quantities.most_common():
            product = ProductModel.query.filter_by(id=_id).first()
            if not product:
                return BadRequest

            products.append(ProductsInOrder(product_id=_id, quantity=count))

        order = OrderModel(products=products)

        db.session.add(order)
        db.session.commit()
        return order
