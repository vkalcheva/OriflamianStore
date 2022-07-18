
from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.order import OrderManager


class OrderResource(Resource):
    @auth.login_required
    def post(self):
        data = request.get_json()
        current_user = auth.current_user()
        new_order = OrderManager.create(data, current_user)
        return new_order, 201



