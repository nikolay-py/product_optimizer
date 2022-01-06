import httpx
from bs4 import BeautifulSoup

from .omit_list import omit_list

start_url = "https://www.okeydostavka.ru/spb/catalog"


# Запросить страницу в текстовом формате
def get_html(url):
    try:
        result = httpx.get(url)
        result.raise_for_status()
        return result.text

    except(httpx.RequestError, ValueError):
        print(f"Сетевая ошибка: {url}")
        return False


def get_links():
    html = get_html(start_url)
    if html:
        links_list = []
        soup = BeautifulSoup(html, 'html.parser')

        # Берем все ссылки во всех классах ul
        for item in soup.find_all('ul', class_='categoryList'):
            for ref in item.find_all('a'):
                # Получаем ссылку и убираем принадлежность к городу
                link_category = ref['href']
                index_category = link_category.find('/spb') + 4
                clean_category = link_category[index_category:]
                # Поверяем, что url каталога не в списке исключений
                if clean_category not in omit_list:
                    full_url = get_full_url(clean_category)
                    links_list.append(full_url)

        return links_list


# Склейка url адреса.
# Стартовая ссылка создает данные по одному городу.
# Разбиение адреса при обработке данных и склейка здесь
#  - дают возможность замены города
# Москва ='msk', Питер ='spb'
def get_full_url(link_category, city='msk'):
    # full_url = f"https://www.okeydostavka.ru/{city}{link_category}"
    full_url = f"https://www.okeydostavka.ru/{city}{link_category}"
    return full_url
