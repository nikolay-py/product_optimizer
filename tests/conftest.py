import pytest
from app import create_app
from database import migrate, drop
from sqlalchemy_utils import create_database, database_exists, drop_database
from database import get_db

import os
import time

@pytest.fixture(scope='function')
def db():
    """Create new test db for testing session."""
    db_url = os.environ.get('DB_URL')
    try:
        db_exists = database_exists(db_url)
    except Exception as exc:
        pytest.skip(f'Test skipped due to error: {exc}')

    if db_exists:
        drop_database(db_url)

    migrate()
    yield get_db()
    time.sleep(1)
    drop()
    drop_database(db_url)



@pytest.fixture
def client(db):
    app = create_app(create_db=False)
    with app.test_client() as client:
        client.db = db
        yield client
