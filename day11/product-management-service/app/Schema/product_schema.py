from locale import currency
from typing_extensions import Required
from xmlrpc.client import Boolean
from marshmallow import Schema, fields
from marshmallow.validate import Length, OneOf


class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    description = fields.Str(validate=Length(min=20, max=300))
    price = fields.Int(required=True, validate=Length(min=1, max=99999))
    currency = fields.Str(required=True, validate=OneOf(['€','₹']))
    stock = fields.Int(required=True, validate=Length(min=1, max=999))
    active = fields.Boolean(Required=True)