import pytest
from webapp import create_app
from config import TestConfig
from webapp.extensions import db


@pytest.fixture(scope='module')
def test_client():
    app = create_app(create_db=False)
    app.config.from_object(TestConfig)

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            setattr(client, 'db', db)

            yield client

            db.session.remove()
            db.drop_all()
