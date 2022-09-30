from werkzeug.exceptions import HTTPException

class InvalidProductPayload(HTTPException):
    def __init__(self, message="Product payload has invalid input", code=400):
        self.message = message
        self.code = code
        super().__init__()

class ProductExistsException(HTTPException):
    def __init__(self, message="Product already exists in the DB", code=400):
        self.message = message
        self.code = code
        super().__init__()

class ProductNotFoundException(HTTPException):
    def __init__(self, message="Product not found in the DB", code=400):
        self.message = message
        self.code = code
        super().__init__()

