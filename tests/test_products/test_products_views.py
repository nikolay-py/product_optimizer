from flask.testing import FlaskClient
from project.products.crud import create_product
from project.products.models import Product



def test_products_endpoint(client: FlaskClient):
    assert len(client.db.query(Product).all()) == 0
    create_product(
        client.db,
        name='test',
        link_photo='link',
        price=100,
        description='test desc',
        category='test-category',
    )
    res = client.get('/api/products/')
    assert res.status_code == 200
    assert len(res.get_json()) == 1

def test_products_endpoint2(client: FlaskClient):
    assert len(client.db.query(Product).all()) == 0
    create_product(
        client.db,
        name='test',
        link_photo='link',
        price=100,
        description='test desc',
        category='test-category',
    )
    res = client.get('/api/products/')
    assert res.status_code == 200
    assert len(res.get_json()) == 1

    #написать тест работы фильтров check filter