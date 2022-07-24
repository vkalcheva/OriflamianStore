from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.category import CategoryManager
from models import RoleType
from schemas.responses.category import CategoryResponseSchema
from utils.decorators import permission_required


class CategoryResource(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def post(self):
        data = request.get_json()
        current_user = auth.current_user()

        new_product = CategoryManager.create(data, current_user)
        return CategoryResponseSchema().dump(new_product), 201