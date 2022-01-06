"""Retrieving data for a recipe."""
from typing import Dict, List, Union

import bs4
import httpx
from bs4 import BeautifulSoup


def get_html(url: str) -> Union[str, bool]:
    """We get raw materials for the soup."""
    with httpx.Client(timeout=10.0) as client:
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
