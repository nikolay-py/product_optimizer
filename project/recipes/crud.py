from sqlalchemy.orm.session import Session
from .models import Recipe
from sqlalchemy.orm import Session


def create_product(db: Session, name, url, product_list):
    new_recipe = Recipe(
        name=name,
        url=url,
        product_list=product_list
    )
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

def get_product(db: Session, url=None): #URL вместо категории вернуть по URL
    if url:
        return db.query(Recipe).filter_by(url=url)
    return db.query(Recipe).all()

