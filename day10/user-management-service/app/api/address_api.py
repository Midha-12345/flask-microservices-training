from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from ..database import get_db_connection, close_db_connection, commit_and_close_db_connection
from ..database import address_db
from ..schemas.address_schema import AddressSchema
from ..exceptions import InvalidAddressPayload,AddressNotFoundException
from ..models.address import Address
from app import restful_api, db
 

address_schema = AddressSchema()

class AddressApi(Resource):
	decorators = [jwt_required()]
	def get(self, id):
		address = Address.query.get(id)
		if not address:
			raise AddressNotFoundException(f"Address with ID [{id}] not found in DB")
		return address.to_json()

	def put(self, id):
		address = Address.query.get(id)
		if not address:
			raise AddressNotFoundException(f"Address with ID [{id}] not found in DB")
		errors = address_schema.validate(request.json)
		if errors:
			raise InvalidAddressPayload(errors, 400)
		updated_address = Address.from_json(request.json)
		address.name = updated_address.name
		address.email = updated_address.email
		address.age = updated_address.age
		#address.password = flask_bcrypt.generate_password_hash(updated_user.password).decode('utf-8')
		db.session.commit()
		return address.to_json()



		conn = get_db_connection()
		address_db.get_address_details(conn, id) #validate id address exists befire udpate
		address_db.update_address_details(conn, id, Address.from_json(request.json))
		address = address_db.get_address_details(conn, id)
		commit_and_close_db_connection(conn)
		return address

	def delete(self, id):
		conn = get_db_connection()
		address = address_db.get_address_details(conn, id)
		address_db.delete_address(conn, id)
		commit_and_close_db_connection(conn)
		return {'message': f'Address [{address["id"]}] deleted from the database'}

restful_api.add_resource(AddressApi, '/api/addresses/<int:id>')