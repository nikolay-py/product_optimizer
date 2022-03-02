from typing import Optional
from webapp.extensions import db
from flask import Blueprint, render_template, request
from webapp.parsers.crud import get_goods
from webapp.recipes.crud import create_recipe, get_recipe
from webapp.recipes.recipes_menunedeli import get_html, get_menu, get_menu_name

from webapp.recipes.models import Recipe

recipes_bp = Blueprint('products', __name__, template_folder='./templates')


@recipes_bp.route('/', methods=['GET','POST'])
def products() -> Optional[str]:
    if request.method == 'GET':
        return render_template(
            'Recipe_Form.html',
            title='My products'
        )
    if request.method == 'POST':
        recipe_url: Optional[str]
        recipe_url = request.form.get('url')
        recipes = get_recipe(db.session, recipe_url)
        if len(recipes) == 1:
            print('Рецепт есть в базе')

        else:
            print('Запущен парсер')
            html = get_html(recipe_url)
            if 'menunedeli' in recipe_url:
                name = get_menu_name(html)
                ingredients = get_menu(html)  # https://menunedeli.ru/recipe/vengerskij-sup-gulyash-s-kartofelem/
            create_recipe(db.session, name, recipe_url, ingredients)
            recipes = get_recipe(db.session, recipe_url)
            print(f'\n\n\n', recipes, '\n\n\n')

        recipe_id = recipes[0].id
        name = recipes[0].name
        ingredients = recipes[0].product_list
        # for items in ingredients:
        #     print(items.get('item'))
        #     print(items.get('qty'))
        #     print(items.get('units'))

        return render_template(
            'Recipe_Form.html',
            title='Response',
            name=name,
            recipe_id=recipe_id,
            ingredients=ingredients
        )


@recipes_bp.route('/<int:recipe_id>', methods=['GET'])
def get_products_step(recipe_id: int) -> str:
    """Getting a recipe by ID from the database."""
    recipe = db.session.query(Recipe).filter(Recipe.id == recipe_id).first()
    ingredients = recipe.product_list
    name = recipe.name
    products = get_goods(ingredients,10)

    return render_template(
        'goods_form.html',
        title='Goods',
        name=name,
        products=products
    )
