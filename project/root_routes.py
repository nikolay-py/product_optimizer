from flask import Blueprint

from project.recipes.routes import recipes_bp

root = Blueprint('root', __name__,)
root.register_blueprint(recipes_bp)
