from marshmallow import Schema, fields


class ProductSchemaRequest(Schema):
    name = fields.String(required=True)
