from flask import Blueprint
from project.recipes.routes import recipes_api_bp #products_bp

from project.recipes.routes import recipes_api_bp

api = Blueprint('api', __name__, url_prefix='/api')
api.register_blueprint(recipes_api_bp)

content = Blueprint('content', __name__)
# content.register_blueprint(products_bp)


root = Blueprint('root', __name__,)
root.register_blueprint(api)
root.register_blueprint(content)
