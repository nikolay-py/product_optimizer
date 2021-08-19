from flask import Blueprint
from project.recipes.routes import recipes_bp  # products_bp #TODO Проверить recipes_bp или API
from project.parsers.routes import goods_bp  # goods_bp

root = Blueprint('root', __name__,)
root.register_blueprint(recipes_bp)
root.register_blueprint(goods_bp)

# Создали blueprint goods_bp, и прявзяали к root,
# чтобы созадавалась база данных для goods, при регистрации
# root в приложении app.
# Можно было отдельно зарег-ть базу в приложении

# Заготовка на создание api
# api = Blueprint('api', __name__, url_prefix='/api')
# api.register_blueprint(recipes_bp)

# content = Blueprint('content', __name__)
# # content.register_blueprint(products_bp)
# root.register_blueprint(api)
# root.register_blueprint(content)
