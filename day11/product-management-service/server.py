from app import app, db
from app.api.products_api import ProductsApi
from app.api.product_api import ProductApi




if __name__ == '__main__':
    db.create_all()
    app.run()