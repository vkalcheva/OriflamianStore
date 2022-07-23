from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models import State
from schemas.responses.product import ProductResponseSchema
from schemas.responses.user import ClientResponseSchema


class OrderSchemaResponse(Schema):
    id = fields.Int(required=True)
    created_on = fields.DateTime(required=True)
    status = EnumField(State, by_value=True)
    client = fields.Nested(ClientResponseSchema, many=True)

    products = fields.List(fields.Nested(ProductResponseSchema), many=True)
