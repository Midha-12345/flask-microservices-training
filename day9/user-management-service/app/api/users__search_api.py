from flask_restful import Resource
from flask_jwt_extended import jwt_required
from ..database import get_db_connection, close_db_connection, commit_and_close_db_connection
from ..database import user_db
from app import restful_api,app

#log the email as info

#add error log stating that the user was not found in DB


#log warning that anonymous user is accessing the data


class UsersSearchApi(Resource):
	decorators = [jwt_required(optional=True)]	#Add appropriate decorators
	def get(self,email):
		email = email
		app.logger.info(f"record requested by {email}")     #log the email as info
		conn = get_db_connection()
		if jwt_required():
			app.logger.info(f"Info {email} is accessing the data")
			user = user_db.get_user_details_from_email(conn, email)
			close_db_connection(conn)
			return user.to_json()
		else:
			app.logger.error(f"Error!  the provided email is not in database {email}")
			app.logger.warning(f"Warning!, this anonymous {email} is accessing the data")
			user = f'Hello: {email}'
			return user

		#pass #Add logic to give full user details if accesed by a user with valid token else return just name and email

# Uncomment the below line by adding a valid url mapping for the user search API
restful_api.add_resource(UsersSearchApi, '/api/users/search/<string:email>')