from flask import Blueprint
<<<<<<< HEAD
=======
from project.recipes.routes import recipes_api_bp  # products_bp
from project.parsers.routes import goods_api_bp  # goods_bp


api = Blueprint('api', __name__, url_prefix='/api')
api.register_blueprint(recipes_api_bp)

content = Blueprint('content', __name__)
# content.register_blueprint(products_bp)
>>>>>>> ac3bcc4a01ac9ce2da417465652ead804e3a8c72

from project.recipes.routes import recipes_bp

root = Blueprint('root', __name__,)
<<<<<<< HEAD
root.register_blueprint(recipes_bp)
=======
root.register_blueprint(api)
root.register_blueprint(content)

# Создали blueprint goods_api_bp, и прявзяали к root,
# чтобы созадавалась база данных для goods, при регистрации
# root в приложении app.
# Можно было отдельно зарег-ть базу в приложении
root.register_blueprint(goods_api_bp)
>>>>>>> ac3bcc4a01ac9ce2da417465652ead804e3a8c72
