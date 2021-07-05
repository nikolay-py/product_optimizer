import sqlalchemy as sa
from database import Base

<<<<<<< HEAD
class Recipe(Base):
    __tablename__ = 'recipes'
=======
class Product(Base):

    __tablename__ = 'products'
    
>>>>>>> ac3bcc4a01ac9ce2da417465652ead804e3a8c72
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    url = sa.Column(sa.String, nullable=False)
    product_list = sa.Column(sa.Text, nullable=False)

    def __repr__(self):
        return f'<Item {self.name} {self.id}>'
