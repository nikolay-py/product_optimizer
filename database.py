"""Functional for working with a database."""
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.environ.get('DB_URL')
engine = create_engine(DB_NAME, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def migrate() -> None:
    """Create db."""
    Base.metadata.create_all(engine)


def drop() -> None:
    """Drop db."""
    Base.metadata.drop_all(engine)


def get_db() -> Session:
    """Get Session."""
    return SessionLocal()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
