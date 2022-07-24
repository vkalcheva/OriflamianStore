from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.order import OrderManager
from models import RoleType
from schemas.request.order import OrderSchemaRequest
from schemas.responses.order import OrderSchemaResponse
from utils.decorators import validate_schema, permission_required


class OrderResource(Resource):
    @auth.login_required
    @permission_required(RoleType.client)
    @validate_schema(OrderSchemaRequest)
    def post(self):
        data = request.get_json()
        current_user = auth.current_user()  # object client is not iterable
        new_order = OrderManager.create(data, current_user)

        return OrderSchemaResponse().dump(new_order), 201


class ApproveOrderResource(Resource):
    @auth.login_required
    def put(self, id):
        OrderManager.approve(id)
        return 204


class RejectOrderResource(Resource):
    @auth.login_required
    def put(self, id):
        OrderManager.reject(id)
        return 204
