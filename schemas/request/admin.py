from marshmallow import Schema, fields, validate

from schemas.request.user import UserSchema


class RequestRegisterAdminSchema(UserSchema):
    first_name = fields.Str(required=True, validate=validate.Length(min=2, max=20))
    last_name = fields.Str(required=True, validate=validate.Length(min=2, max=20))
    phone = fields.Str(required=True, validate=validate.Length(min=14, max=14))


class RequestLoginAdminSchema(UserSchema):
    pass
