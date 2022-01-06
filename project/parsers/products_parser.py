import logging

import httpx
from bs4 import BeautifulSoup
from project.parsers.link_list import get_links
from project.parsers.price import get_price


def run_parser():
    """Entrypoint."""
    logging.info('Start parser')

    link_list = get_links()
    # Открываем сессию на запрос страниц
    with httpx.Client(timeout=10.0) as client:
        for url in link_list:
            try:
                res = client.get(url)
                res.raise_for_status()
                result = res.text
                print(f'Счтиываю {url}')
            except(httpx.RequestError, ValueError) as e:
                print(f"Сетевая ошибка: {e} url: {url}")
                result = False

            if result is not False:
                soup = BeautifulSoup(result, 'html.parser')
                get_price(soup)
