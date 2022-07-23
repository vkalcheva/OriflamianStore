from marshmallow import Schema, fields


class ClientResponseSchema(Schema):
    id = fields.Integer(required=True)
    first_name = fields.String(required=True)
