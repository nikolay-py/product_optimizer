"""Application initialization."""
import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    """Base initialization config."""

    DEBUG = False
    SECRET_KEY = 'j;j;j;55646^*7sdfsf'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
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
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_TEST')
