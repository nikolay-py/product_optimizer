from .models import Good
from sqlalchemy.exc import SQLAlchemyError
from database import SessionLocal


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


# def get_product(db: Session, category=None):
#     if category:
#         return db.query(Product).filter_by(category=category)
#     return db.query(Product).all()

