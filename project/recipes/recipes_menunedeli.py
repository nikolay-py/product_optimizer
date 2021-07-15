import pprint, httpx

from bs4 import BeautifulSoup

def get_html(url):
    with httpx.Client(timeout=10.0) as client:
        try:
            result = client.get(url)
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

if __name__ == "__main__":
    html = get_html('https://menunedeli.ru/recipe/vengerskij-sup-gulyash-s-kartofelem/')
    if html:
        name = get_menu_name(html)
        ingredients = get_menu(html)
        print(name)
        pprint.pprint(ingredients)
