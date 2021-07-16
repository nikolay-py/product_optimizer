from sqlalchemy import Column, Integer, String

from database import Base


class Good(Base):
    __tablename__ = 'goods'

    id = Column(Integer(), primary_key=True)
    category = Column(String(), nullable=False)
    name = Column(String(), index=True, nullable=False)
    price = Column(Integer(), nullable=False)
    weight = Column(Integer(), nullable=False)
    units = Column(String(), nullable=False)
    price_per_kg = Column(Integer(), nullable=False)

    def __repr__(self):
        return f'<Good {self.name} {self.category}>'
