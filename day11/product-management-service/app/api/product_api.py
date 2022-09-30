from itertools import product
from flask import request, jsonify	
from flask_restful import Resource
from ..models.product import Product
from app import restful_api, db
from app.exceptions import InvalidProductPayload, ProductExistsException,ProductNotFoundException
from ..schemas.product_schema import ProductSchema

product_schema = ProductSchema()

class ProductApi(Resource):
	def get(self, name):
		product = Product.query.get(name)
		if not product:
			raise ProductNotFoundException(f"Product with name [{product}] not found in DB")
		return product.to_json()

	def put(self, id):
			product = Product.query.get(id)
			if not product:
				raise ProductNotFoundException(f"Product with ID [{id}] not found in DB")
			errors = product_schema.validate(request.json)
			if errors:
				raise InvalidProductPayload(errors, 400)
			updated_product = Product.from_json(request.json)
			product.id = updated_product.id
			product.name = updated_product.name
			product.description = updated_product.description
			product.price = updated_product.price
			product.currency = updated_product.currency
			product.stock = updated_product.stock
			product.active = updated_product.active
			db.session.commit()
			return product.to_json()

	def delete(self, id):
		product = Product.query.get(id)
		db.session.delete(product)
		db.session.commit()
		return {'message': f'Product [{product.id}] deleted from the database'}

restful_api.add_resource(ProductApi, '/api/products/<int:id>')