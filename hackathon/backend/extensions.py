from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

def init_extensions(app):
    """
    Initialize all Flask extensions with the app instance.
    """
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)  # Allow cross-origin requests
