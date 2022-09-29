import os

_deployed_env_ = os.environ.get("FLASK_ENV", default=None)
print(f"Environment: [{_deployed_env_}]")

class Config(object):
     
    UMS_ADMIN_EMAIL = 'saurav@gmail.com'
    UMS_ADMIN_PASSWORD = 'saurav'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/user-management-db'

class DevelopmentConfig(Config):
    DATABASE_URI = 'user-management-dev.db'
    DEBUG = True