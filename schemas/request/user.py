from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=8, max=20))


class RequestRegisterUserSchema(UserSchema):
    first_name = fields.Str(required=True, validate=validate.Length(min=2, max=20))
    last_name = fields.Str(required=True, validate=validate.Length(min=2, max=20))


class RequestLoginUserSchema(UserSchema):
    pass

