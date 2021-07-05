from flask import Blueprint

# Чтобы создались колонки модели Good при создании общей базы,
# импортируем ее сюда, далее информация о модели потянется
# в app при регистрации Blueprint goods_api_bp
from .models import Good

goods_api_bp = Blueprint('goods_api', __name__, url_prefix='/goods')


@goods_api_bp.route('/', methods=['GET'])
def goods_api():
    pass
