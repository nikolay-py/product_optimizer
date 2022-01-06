"""Actions for Recipe model."""
from typing import Dict, List, Union

from sqlalchemy.orm import Session

from .models import Recipe


def create_recipe(db: Session, name: str, url: str,
                  product_list: List[Dict[str, Union[str, float]]]) -> Recipe:
    """Save model in db."""
    new_recipe = Recipe(
        name=name,
        url=url,
        product_list=product_list
    )
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe


def get_recipe(db: Session, url: str = None) -> Recipe:
    """Request to the base."""
    if url:
        return db.query(Recipe).filter_by(url=url).all()
    return db.query(Recipe).all()
