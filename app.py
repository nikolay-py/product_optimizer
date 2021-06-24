from flask import Flask

from project.root_routes import root
from database import migrate
from dotenv import load_dotenv
load_dotenv()


def create_app(create_db=True):
    app = Flask(__name__)
    app.register_blueprint(root)
    if create_db:
        migrate()
    return app
