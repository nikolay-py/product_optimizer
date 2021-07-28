# Product_optimizer
Продуктовый оптимизатор - это сервис оптимизации списка продуктов под список рецептов.
Пользователь копирует url понравившегося рецепта блюда с сайта ["Меню недели"](https://menunedeli.ru/) и получает список продуктов к покупке, с указнием цены, а также возможностью выбрать/уточнить товар.

Цеы на товары парсятся с сайта [ОКЕЙ-доставка](https://www.okeydostavka.ru/s)


## Установка

### Install dependencies
`pip install pipenv`
`pipenv install --dev`
''

### Run app
`export FLASK_APP=app FLASK_ENV=development & flask run`
