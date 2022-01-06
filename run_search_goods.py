"""A utility for experimenting with searching."""
from project.parsers.crud import get_goods
from project.parsers.search_goods import db
from project.recipes.models import Recipe


if __name__ == "__main__":
    recipe = db.query(Recipe).filter(Recipe.id == 2).first().product_list
    goods_list = get_goods(recipe,10)
    for inhidient in goods_list:
        print('----------------------------------------------')
        print(inhidient)
