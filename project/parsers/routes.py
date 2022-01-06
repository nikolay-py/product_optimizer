"""Routs for work with db Goods."""
from flask import Blueprint

# Чтобы создались колонки модели Good при создании общей базы,
# импортируем ее сюда, далее информация о модели потянется
# в app при регистрации Blueprint goods_api_bp
from .models import Good
from project.parsers.products_parser import run_parser
goods_bp = Blueprint('goods_bp', __name__, url_prefix='/goods')


@goods_bp.route('/base', methods=['GET'])
def goods() -> str:
    """Runs parser."""
    run_parser()
    return 'Наполнение базы продуктов окончен, можете \
        вернуться на страртовую страницу и загурзить рецепт'
