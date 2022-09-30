from flask import request, jsonify	
from flask_restful import Resource
from ..models.product import Product
from app import restful_api, db
from app.exceptions import InvalidProductPayload, ProductExistsException,ProductNotFoundException
from ..schemas.product_schema import ProductSchema

product_schema = ProductSchema()

class ProductsApi(Resource):

	def get(self):
		return [product.to_json() for product in Product.query.all()]

	def post(self):
		errors = product_schema.validate(request.json)
		if errors:
			raise InvalidProductPayload(errors, 400)
		existing_product = Product.query.filter_by(name=request.json.get('name')).first()
		if(existing_product is not None):
			raise ProductExistsException(f"Product [{existing_product.name}] already exists")
		product = Product.from_json(request.json)
		db.session.add(product)
		db.session.commit()
		new_product = Product.query.filter_by(name=product.name).first()
		return new_product.to_json(), 201

restful_api.add_resource(ProductsApi, '/api/products')
