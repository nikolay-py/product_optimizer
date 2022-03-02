from webapp.extensions import db
from sqlalchemy.exc import SQLAlchemyError
from webapp.parsers.models import Good


def save_data(goods:Good) -> None:
    """Image data save model."""
    try:
        db.session.add(goods)
        db.session.commit()
        db.session.refresh(goods)
    except SQLAlchemyError as e:
        print(f"Ошибка {e} при венсении в базу данных {goods}")
        db.session.rollback()
        raise
