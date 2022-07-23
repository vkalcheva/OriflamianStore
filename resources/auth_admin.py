from flask import request
from flask_restful import Resource


from managers.admin import AdminManager
from schemas.request.admin import RequestRegisterAdminSchema, RequestLoginAdminSchema
from utils.decorators import validate_schema


class CreateAdminResource(Resource):
    @validate_schema(RequestRegisterAdminSchema)
    def post(self):
        data = request.get_json()
        token = AdminManager.create_admin(data)
        return {"token": token}, 201


class LoginAdminResource(Resource):
    @validate_schema(RequestLoginAdminSchema)
    def post(self):
        data = request.get_json()
        token = AdminManager.login_admin(data)
        return {"token ": token}, 200
