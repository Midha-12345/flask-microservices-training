from locale import currency
from xmlrpc.client import Boolean
from app import db

class Product(db.Model):
    __tablename__ = 'Product'
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(required=True)
    description = db.Column(db.String(min=20, max=300))
    price = db.Column(db.Integer(min=1, max=99999))
    currency = db.Column(db.Oneof(['€','₹','$']), required=True)
    stock = db.Column(db.Integer(min=1, max=999), required=True)
    active = db.Column(db.Boolean(required=True))

    def __init__(self, id, name, description, price, currency, stock, active):
            self.id = id
            self.name = name
            self.description = description
            self.price = price
            self.curreny = currency
            self.stock = stock
            self.active = active


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'currency': self.currency,
            'stock': self.stock,
            'active': self.active
        }

    @staticmethod
    def from_json(json_dct):
      return Product(json_dct['id'],
                    json_dct['name'],
                    json_dct['description'],
                    json_dct['price'],
                    json_dct['currency'],
                    json_dct['stock'],
                    json_dct['active'])    