from os import name

from sqlalchemy.orm.session import Session
from project.products.crud import create_product
from project.products.models import Product


def test_create_product(db: Session):
    create_product(
        db,
        name='test',
        link_photo='link',
        price=100,
        description='test desc',
        category='test-category',
    )
    assert len(db.query(Product).all()) == 1

def test_create_product_price(db: Session):
    expected_price = 500
    product = create_product(
        db,
        name='test',
        link_photo='link',
        price=expected_price,
        description='test desc',
        category='test-category',
    )
    assert isinstance(product.price, int)
    assert product.price == expected_price
 