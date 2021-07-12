import pprint
import requests
import sqlalchemy as sa
from bs4 import BeautifulSoup
from database import Base
from .models import Recipe

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False

def get_soup(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_menu_name(html):
    name = get_soup(html).find('h1').text
    return name

def get_menu(html):
    ingredients_li = get_soup(html).find('ul', class_="ingredients-lst").findAll('li')
    all_ingredients = []
    for li in ingredients_li:
        name = li.find(class_='name').text
        value = li.find(class_='value').text
        type = li.find(class_='type').text

        all_ingredients.append({
            'item': name,
            'qty': value,
            'units': type
        })
    return all_ingredients

def save_recipe(name, url, ingredients):
    recipe_exists = Recipe.query.filter(Recipe.url == url).count()
    print(recipe_exists)
    if not recipe_exists:
        new_recipe = Recipe(name=name, url=url, product_list=ingredients)
        sa.session.add(new_recipe)
        sa.session.commit()

if __name__ == "__main__":
    html = get_html('https://menunedeli.ru/recipe/vengerskij-sup-gulyash-s-kartofelem/')
    if html:
        name = get_menu_name(html)
        ingredients = get_menu(html)
        print(name)
        pprint.pprint(ingredients)