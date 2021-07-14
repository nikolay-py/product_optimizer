from .models import Good
from sqlalchemy.exc import SQLAlchemyError
from database import SessionLocal
from .search_goods import get_several_variants, limit_result


def create_goods(items):
    goods = Good(
        category=items['key'],
        name=items['name'],
        price=items['price'],
        weight=items['weight'],
        units=items['units'],
        price_per_kg=items['price_per_kg']
    )
    with SessionLocal() as session:
        session.add(goods)
        try:
            session.commit()
            session.refresh(goods)
        except SQLAlchemyError as e:
            print(f"Ошибка {e} при венсении в базу данных {goods}")
            session.rollback()
            raise


def get_goods(recipe, length_list=10):
    # На вход получаем запрос в види списка словарей,
    # пройдемся по каждому из них
    for ingredient in recipe:
        # Получаем общий результат поиска по названию ингридиента
        general_list = get_several_variants(ingredient['item'])
        # Сокращаем список результатов поиска
        limited_list = limit_result(general_list,length_list)
        # Наполняем словарь ингридента подходящими товарами
        ingredient['goods'] = limited_list

    return recipe
