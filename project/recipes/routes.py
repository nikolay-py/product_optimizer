import requests
from flask import Blueprint, request, Response, render_template
from database import get_db
from .models import Product
from flask import json
from flask import request
from project.recipes.crud import create_product, get_product
from project.recipes.recipes_gastronom import get_html, get_recipe_gastr
from project.recipes.recipes_menunedeli import get_recipe_menu

recipes_api_bp = Blueprint('products_api', __name__, url_prefix='/recipes') #
# products_bp = Blueprint('products', __name__, url_prefix='/products', template_folder='./templates')

@recipes_api_bp.route('/', methods=['POST', 'GET'])
def products_api():
    db = get_db()
    if request.method == 'GET':
        url = request.args.get('url')
        print(url)
        html = get_html(url)
        if 'gastronom' in url:
            ingredients = get_recipe_gastr(html) #https://www.gastronom.ru/recipe/26403/borsch-bez-kapusty
            print(ingredients)
        if 'menunedeli' in url:
            ingredients = get_recipe_menu(html) #https://menunedeli.ru/recipe/vengerskij-sup-gulyash-s-kartofelem/
            print(ingredients)
        response = Response(
            response=json.dumps(ingredients),
            status=200,
            mimetype='application/json'
        )
        return response

    if request.method == 'POST':
        data_json = json.loads(request.data)
        print(data_json)
        new_product = create_product(db, **data_json)
        
        response = Response(
            response=json.dumps({'status': 'OK'}),
            status=201,
            mimetype='application/json'
        )
        return response


# @products_bp.route('/', methods=['GET'])
# def products():
#     db = get_db()
#     if request.method == 'GET':
#         products = db.query(Product).all()
#         return render_template(
#             'products_page.html',
#             title='My products',
#             products=products,
#         )