import requests
from flask import Blueprint, request, Response, render_template
from database import get_db
from .crud import get_recipe, create_recipe
from .models import Recipe
from flask import json
from flask import request
from project.recipes.crud import create_recipe, get_recipe
from project.recipes.recipes_gastronom import get_html, get_recipe_gastr
from project.recipes.recipes_menunedeli import get_menu, get_menu_name, save_recipe
# ----------------------------
from project.parsers.crud import get_goods

recipes_bp = Blueprint('products', __name__, template_folder='./templates')

@recipes_bp.route('/', methods=['GET','POST'])
def products():
    db = get_db()
    if request.method == 'GET':
        return render_template(
            'Recipe_Form.html',
            title='My products'
        )
    if request.method == 'POST':
        recipe_url = request.form.get('url')
        recipes = get_recipe(db, recipe_url)
        if len(recipes) == 1:
            print('Рецепт есть в базе')

        else:
            print('Запущен парсер')
            html = get_html(recipe_url)
            if 'gastronom' in recipe_url:
                ingredients = get_recipe_gastr(html) #https://www.gastronom.ru/recipe/26403/borsch-bez-kapusty
                print(ingredients)
            if 'menunedeli' in recipe_url:
                name = get_menu_name(html)
                ingredients = get_menu(html) #https://menunedeli.ru/recipe/vengerskij-sup-gulyash-s-kartofelem/
            create_recipe(db, name, recipe_url, ingredients)
            recipes = get_recipe(db, recipe_url) 

        name = recipes[0].name
        ingredients = recipes[0].product_list
        for items in ingredients:
            # print(type(items))
            # for item in items:
            print(items.get('item'))
            print(items.get('qty'))
            print(items.get('units'))

        return render_template(
            'Recipe_Form.html',
            title='Response',
            name=name,
            ingredients=ingredients
        )


@recipes_bp.route('/<int:recipe_id>', methods=['GET'])
def get_products_step(recipe_id):
    db = get_db()
    recipe = db.query(Recipe).filter(Recipe.id == recipe_id).first()
    ingredients = recipe.product_list
    name = recipe.name
    products = get_goods(ingredients,10)

    return render_template(
        'goods_form.html',
        title='Goods',
        name=name,
        products=products
    )
