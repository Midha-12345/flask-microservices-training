import os

_deployed_env_ = os.environ.get("FLASK_ENV", default=None)
print(f"Environment: [{_deployed_env_}]")

class Config(object):
     
    UMS_ADMIN_EMAIL = 'saurav@gmail.com'
    UMS_ADMIN_PASSWORD = 'saurav'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/product-management-db'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/product-management-db'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/product-management-db'
    
    DEBUG = True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/product-management-db'
    TESTING = True

def load_configuration(app):
    print(_deployed_env_)
    if (_deployed_env_ == None):
        app.config.from_object(DevelopmentConfig)
    elif (_deployed_env_ == 'dev'):
        app.config.from_object(DevelopmentConfig)
    elif (_deployed_env_ == 'testing'):
        app.config.from_object(TestingConfig)
    elif (_deployed_env_ == 'production'):
        app.config.from_object(ProductionConfig)
    else:
        raise RuntimeError('Unknown environment setting provided.') 