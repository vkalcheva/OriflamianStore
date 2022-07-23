from marshmallow import Schema, fields


class ProductResponseSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    price = fields.Float(required=True)
    description = fields.String(required=True)
    photo_url = fields.String(required=True)
