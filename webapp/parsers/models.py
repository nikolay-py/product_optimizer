"""Models Good."""
from webapp.extensions import db


class Good(db.Model):
    __tablename__ = 'goods'

    id = db.Column(db.Integer(), primary_key=True)
    category = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), index=True, nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    weight = db.Column(db.Integer(), nullable=False)
    units = db.Column(db.String(), nullable=False)
    price_per_kg = db.Column(db.Integer(), nullable=False)

    def __repr__(self) -> str:
        return f'<Good {self.name} {self.category}>'
