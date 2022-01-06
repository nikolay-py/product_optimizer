"""Create Flask-app."""
from database import migrate
from dotenv import load_dotenv
from flask import Flask
from project.root_routes import root

load_dotenv()


def create_app(create_db: bool = True) -> Flask:
    """Create app."""
    app = Flask(__name__)
    app.register_blueprint(root)
    if create_db:
        migrate()
    return app
