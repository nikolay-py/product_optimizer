import requests
import pprint
from bs4 import BeautifulSoup
# from regex import check_int, split_units TODO REGEX.PY

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False

def get_recipe_menu(html):
    soup = BeautifulSoup(html, 'html.parser')
    ingredients_li = soup.find('ul', class_="ingredients-lst").findAll('li')
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
    # pprint.pprint(all_ingredients)
    return all_ingredients
    

if __name__ == "__main__":
    html = get_html('https://menunedeli.ru/recipe/vengerskij-sup-gulyash-s-kartofelem/')
    if html:
        ingredients = get_recipe(html)
        pprint.pprint(ingredients)