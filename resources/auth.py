from flask import request
from flask_restful import Resource

from managers.user import ClientManager
from schemas.request.user import RequestRegisterUserSchema, RequestLoginUserSchema
from utils.decorators import validate_schema


class RegisterClient(Resource):
    @validate_schema(RequestRegisterUserSchema)
    def post(self):
        data = request.get_json()
        token = ClientManager.register(data)
        return {"token": token}, 201


class LoginClient(Resource):
    @validate_schema(RequestLoginUserSchema)
    def post(self):
        data = request.get_json()
        token = ClientManager.login(data)
        return {"token": token}, 200
