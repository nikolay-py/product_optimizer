"""Models Recipe and Product."""
import sqlalchemy as sa

from database import Base


class Recipe(Base):
    __tablename__ = 'recipes'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    url = sa.Column(sa.String, nullable=False)
    product_list = sa.Column(sa.JSON, nullable=False)

    def __repr__(self) -> str:
        return '<Recipe {}>'.format(self.name)


class Product(Base):
    __tablename__ = 'products'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    url = sa.Column(sa.String, nullable=False)
    product_list = sa.Column(sa.Text, nullable=False)

    def __repr__(self) -> str:
        return f'<Item {self.name} {self.id}>'
