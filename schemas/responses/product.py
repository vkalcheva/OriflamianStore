from marshmallow import Schema, fields

from schemas.responses.category import CategoryResponseSchema
from schemas.responses.user import AdminResponseSchema


class ProductResponseSchema(Schema):
    id = fields.Int(required=True)
    name = fields.String(required=True)
    price = fields.Float(required=True)
    description = fields.String(required=True)
    photo_url = fields.String(required=True)

    admin = fields.Nested(AdminResponseSchema, many=True)

    category = fields.Nested(CategoryResponseSchema, many=True)
