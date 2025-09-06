from flask import Flask
from extensions import init_extensions, db
from hackathon.backend.routes_auth import bp as auth_bp
from hackathon.backend.routes_projects import bp as proj_bp
from hackathon.backend.routes_tasks import bp as tasks_bp
from hackathon.backend.routes_comments import bp as comments_bp
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET', 'devsecret')

    init_extensions(app)

    # ✅ works in Flask 2.2.5 (removed only in Flask 2.3+)
    @app.before_first_request
    def create_tables():
        db.create_all()

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(proj_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(comments_bp)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)
