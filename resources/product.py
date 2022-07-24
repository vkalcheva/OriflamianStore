from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.product import ProductManager
from models.enums import RoleType
from schemas.responses.product import ProductResponseSchema
from utils.decorators import permission_required


class ProductResource(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def post(self):
        data = request.get_json()
        current_user = auth.current_user()

        new_product = ProductManager.create(data, current_user)
        return ProductResponseSchema().dump(new_product), 201

