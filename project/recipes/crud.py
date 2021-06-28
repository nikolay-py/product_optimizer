from sqlalchemy.orm.session import Session
from .models import Product
from sqlalchemy.orm import Session


def create_product(db: Session, name, link_photo, price, description, category):
    new_product = Product(
        name=name,
        link_photo=link_photo,
        price=price,
        description=description,
        category=category,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_product(db: Session, category=None):
    if category:
        return db.query(Product).filter_by(category=category)
    return db.query(Product).all()

