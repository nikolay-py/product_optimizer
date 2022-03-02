"""A utility for experimenting with searching."""
from webapp.parsers.crud import get_goods
from webapp.parsers.search_goods import db
from webapp.recipes.models import Recipe


if __name__ == "__main__":
    recipe = db.query(Recipe).filter(Recipe.id == 2).first().product_list
    goods_list = get_goods(recipe,10)
    for inhidient in goods_list:
        print('----------------------------------------------')
        print(inhidient)
