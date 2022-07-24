from marshmallow import Schema, fields


class ProductSchemaRequest(Schema):
    name = fields.String(required=True)
    price = fields.Float(required=True)
    description = fields.String(required=True)
    photo_url = fields.String(required=True)
