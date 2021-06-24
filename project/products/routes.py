from flask import Blueprint, request, Response, render_template
from database import get_db
from .models import Product
from flask import json
from flask import request
from project.products.crud import create_product, get_product

products_api_bp = Blueprint('products_api', __name__, url_prefix='/products') #
# products_bp = Blueprint('products', __name__, url_prefix='/products', template_folder='./templates')

@products_api_bp.route('/', methods=['POST', 'GET'])
def products_api():
    db = get_db()
    if request.method == 'GET':
        category = request.args.get('category')
        print(request.args)
        products = [{
            'id': p.id,
            'name': p.name,
            'link_photo': p.link_photo,
            'description': p.description,
            'category': p.category
        } for p in get_product(db, category)]
        response = Response(
            response=json.dumps(products),
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