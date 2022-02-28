from extensions import db
from sqlalchemy.exc import SQLAlchemyError



def save_data(goods) -> None:
    """Image data save model."""
    try:
        db.session.add(goods)
        db.session.commit()
        db.session.refresh(goods)
    except SQLAlchemyError as e:
        print(f"Ошибка {e} при венсении в базу данных {goods}")
        db.session.rollback()
        raise
