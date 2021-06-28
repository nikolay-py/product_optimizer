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

def get_recipe_gastr(html):
    soup = BeautifulSoup(html, 'html.parser')
    ingredients = soup.findAll('li', class_='recipe__ingredient')

    all_ingredients = []
    for item in ingredients:
        ingredient = item.text
        ingredient = ingredient.split(" ", 1) #IMPORTANT: long '–', not short '-'
        qty_units = ingredient[1].lstrip()
        qty_units = qty_units.split(" ", 1)

        all_ingredients.append({
            'item': ingredient[0],
            'qty': qty_units[0],
            'units': qty_units[1]
        })
    return all_ingredients
    

if __name__ == "__main__":
    html = get_html('https://www.gastronom.ru/recipe/26403/borsch-bez-kapusty')
    if html:
        ingredients = get_recipe_gastr(html)
        pprint.pprint(ingredients)

 # TO DO
 # CHECK if start with digit
 # split 5-6 to bigger number
 # change digit to INT     


# URLs
# 'https://www.gastronom.ru/recipe/26403/borsch-bez-kapusty'

# URLs NOT WORKING
# # https://www.gastronom.ru/text/kurica-gril-gotovim-v-duhovke-na-vertele-kak-prigotovit-1013918
# (empty list)
# # https://www.gastronom.ru/recipe/50967/olive-s-rostbifom
# (out of range - Salt w/o units)

# if __name__ == "__main__":
#     html = get_html("https://www.python.org/blogs")
#     if html:
#         get_python_news(html)
#         # with open("python.org.html", "w", encoding="utf8") as f:
#         #     f.write(html)