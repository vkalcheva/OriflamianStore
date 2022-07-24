from flask import request

from db import db
from models import ProductModel


class ProductManager:
    @staticmethod
    def create(data, admin):
        data["admin_id"] = admin.id
        product = ProductModel(**data)
        db.session.add(product)

        return product