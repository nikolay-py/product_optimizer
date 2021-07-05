import requests
from flask import Blueprint, request, Response, render_template
from database import get_db
from .models import Recipe
from flask import json
from flask import request
from project.recipes.crud import create_product, get_product
from project.recipes.recipes_gastronom import get_html, get_recipe_gastr
from project.recipes.recipes_menunedeli import get_recipe_menu

recipes_bp = Blueprint('products', __name__, template_folder='./templates')


@recipes_bp.route('/', methods=['GET','POST'])
def products():
    if request.method == 'GET':
        return render_template(
            'Recipe_Form.html',
            title='My products'
        )
    if request.method == 'POST':
        recipe_url = request.form.get('url')
        html = get_html(recipe_url)
        if 'gastronom' in recipe_url:
            ingredients = get_recipe_gastr(html) #https://www.gastronom.ru/recipe/26403/borsch-bez-kapusty
            print(ingredients)
        if 'menunedeli' in recipe_url:
            ingredients = get_recipe_menu(html) #https://menunedeli.ru/recipe/vengerskij-sup-gulyash-s-kartofelem/
            print(ingredients)


        return render_template(
            'Recipe_Form.html',
            title='Response',
            ingredients=ingredients,
        )