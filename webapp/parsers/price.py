"""We fill the base with products."""
from typing import Union

import bs4

from webapp.parsers.crud import create_goods


def get_catalog_name(soup: bs4) -> Union[str, bool]:
    """Get catalog name."""
    # Получаем имя каталога
    link_page = soup.find(
        'li', class_='breadcrumb-page__item breadcrumb-page__current')
    try:
        catalog_name = link_page.text.strip()
        return catalog_name.lower()
    except AttributeError:
        print('Каталог без имени')
        return False


def get_price_per_kg(price: str, weight: str) -> Union[str, bool]:
    """Price per kg."""
    # Расчет цены за кг и проверка на пустые значения веса
    try:
        price_per_kg = float(price) / float(weight)
        return "{0:.2f}".format(price_per_kg)
    except (ValueError, ZeroDivisionError) as e:
        print('-------------------------------------------------------')
        print(f"Ошибка пустой строки {e}. Цена {price}, Вес{weight}")
        return False


def get_float_price(str_price: str) -> str:
    """Get float price."""
    # Вытаскиваем из разрозненного текста цену
    item_price = ''.join([i for i in str_price if i.isnumeric()])
    price = float(item_price) / 100
    return "{0:.2f}".format(price)


def get_price(soup: bs4) -> None:
    """We get the main dictionary with the price of goods."""
    # Получаем основной словарь с ценой товаров
    items = {}
    catalog_name = get_catalog_name(soup)
    # Находим все классы catalog-item, даже лишние, и перебираем их
    for item in soup.find_all('div', class_='product ok-theme'):
        # Название
        item_title = item.find('div', class_='product-name').find('a')['title'].lower()

        # Цена
        if item.find('span', class_='price label'):
            search = item.find('span', class_='price label').text
            item_price = get_float_price(search)
        else:
            search = item.find('div', class_='product-price').find('span').text
            item_price = get_float_price(search)

        # Вес и единица измерения
        try:
            product_weight = item.find('div', class_='product-weight')
            units = product_weight.find('span').text.strip()

            product_weight.find('span').extract()
            weight = product_weight.text.strip().replace(',', '.')
        except AttributeError:
            units = 'шт'
            weight = 1

        # Цена за кг
        price_per_kg = get_price_per_kg(item_price, weight)

        if price_per_kg is not False and catalog_name is not False:
            # Наполняем словарь
            items = {
                'key': catalog_name,
                'name': item_title,
                'price': float(item_price),
                'weight': weight,
                'units': units,
                'price_per_kg': price_per_kg
            }
            # Сохраняем данные в базу данных
            create_goods(items)
        else:
            print(f"{catalog_name} - {item_title} не учтена")
            print('-------------------------------------------------------')
