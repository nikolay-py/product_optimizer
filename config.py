"""Application initialization."""
import os

from dotenv import load_dotenv

import tempfile


load_dotenv()
BASE_DIR = os.getcwd()


class Config(object):
    """Base initialization config."""

    DEBUG = False
    SECRET_KEY = 'j;j;j;55646^*7sdfsf'
    DB_NAME = os.environ.get('DB_NAME')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')


class ProductionConfig(Config):
    """Production config."""


class DevelopmentConfig(Config):
    """Development config."""

    ENV = "development"
    DEBUG = True


class TestConfig(Config):
    """Test config."""
    TESTING = True
    DB_NAME_TEST = os.environ.get('DB_NAME_TEST')
    # db_name = tempfile.NamedTemporaryFile(prefix="goods_test_", suffix=".db")
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR}/{DB_NAME_TEST}'
    print(SQLALCHEMY_DATABASE_URI)
