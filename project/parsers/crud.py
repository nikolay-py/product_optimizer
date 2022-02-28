"""Working with the product database."""
from typing import Dict, List, Union

# from sqlalchemy.exc import SQLAlchemyError

# from database import SessionLocal

from .models import Good
from .search_goods import get_several_variants, limit_result
from utils import save_data


def create_goods(items: Dict[str, Union[str, float]]) -> None:
    """Save in database."""
    goods = Good(
        category=items['key'],
        name=items['name'],
        price=items['price'],
        weight=items['weight'],
        units=items['units'],
        price_per_kg=items['price_per_kg']
    )
    save_data(goods)


def get_goods(recipe: List[Dict[str, Union[str, float]]], length_list: int = 10) -> List[Dict[str, Union[str, float]]]:
    """Enriching the dictionary goods."""
    # На вход получаем запрос в виде списка словарей,
    # пройдемся по каждому из них
    for ingredient in recipe:
        # Получаем общий результат поиска по названию ингридиента
        general_list = get_several_variants(ingredient['item'])
        # Сокращаем список результатов поиска
        limited_list = limit_result(general_list,length_list)
        # Наполняем словарь ингридента подходящими товарами
        ingredient['goods'] = limited_list

    return recipe
