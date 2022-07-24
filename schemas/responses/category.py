from marshmallow import Schema, fields

from schemas.responses.user import AdminResponseSchema


class CategoryResponseSchema(Schema):
    id = fields.Int(required=True)
    name = fields.String(required=True)
    admin = fields.Nested(AdminResponseSchema, many=True)

