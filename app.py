"""Create Flask-app."""
import os
# from database import migrate
from flask import Flask
from project.root_routes import root
from config import Config
from extensions import db


def create_app(create_db: bool = True) -> Flask:
    """Create app."""
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    db.init_app(app)
    app.register_blueprint(root)
    # if create_db:
    #     migrate()
    return app

db.create_all(app=create_app())

# razdel = print('==============================================================================')
    # for key, value in app.config.items():
    #     print(key, value)
    # razdel
