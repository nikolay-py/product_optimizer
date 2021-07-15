import pprint
from project.recipes.recipes_menunedeli import get_html, get_soup

def get_gast_name(html):
    name = get_soup(html).find('h1').text
    return name

def get_recipe_gastr(html):
    ingredients = get_soup(html).findAll('li', class_='recipe__ingredient')

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