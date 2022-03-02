"""Retrieving data for a recipe."""
from typing import Dict, List, Union

import bs4
import httpx
from bs4 import BeautifulSoup

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
# agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
prox = '176.101.89.226'
# prox = '109.195.23.223'
# prox = '81.24.95.176'
timeout = httpx.Timeout(30.0, connect=10.0)


def get_html(url: str) -> Union[str, bool]:
    """We get raw materials for the soup."""
    with httpx.Client(
            timeout=timeout,
            proxies={'http://': 'http://' + prox},
            headers={'User-Agent': agent}
    ) as client:
        try:
            result = client.get(url)
            result.raise_for_status()
            return result.text
        except(httpx.RequestError, ValueError):
            print("Сетевая ошибка")
            return False


def get_soup(html: str) -> bs4:
    """Get soup object."""
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_menu_name(html: str) -> str:
    """Get menu name."""
    name = get_soup(html).find('h1').text
    return name


def get_menu(html: str) -> List[Dict[str, float]]:
    """Get list ingredients for recipe."""
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
