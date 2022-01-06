# Product_optimizer
Продуктовый оптимизатор - это сервис оптимизации списка продуктов под список рецептов.
#

## Как это работает:
**1. Пользователь копирует url понравившегося рецепта блюда с сайта ["Меню недели"](https://menunedeli.ru/)**
<img src="https://raw.githubusercontent.com/nikolay-py/product_optimizer/main/pictures/1_%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5_url.PNG" alt="Получение url" width="700"/>

**2. Вставляет url в специальное окно нашего сайта. Нажимаем "Получить рецепт"**
<img src="https://raw.githubusercontent.com/nikolay-py/product_optimizer/main/pictures/2_%D0%92%D1%81%D1%82%D0%B0%D0%B2%D0%BA%D0%B0_url.PNG" alt="Вставка_url" width="700"/>

**3. Автоматически поучили ингридиенты, и теперь нажимаем "Получить цены"**
<img src="https://raw.githubusercontent.com/nikolay-py/product_optimizer/main/pictures/3_%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82_%D0%BF%D0%B0%D1%80%D1%81%D0%B8%D0%BD%D0%B3%D0%B0_%D1%80%D0%B5%D1%86%D0%B5%D0%BF%D1%82%D0%B0.PNG" alt="Результат_парсинга_рецепта" width="500"/>

**4. Получили список продуктов к покупке, с указнием цены**
<img src="https://raw.githubusercontent.com/nikolay-py/product_optimizer/main/pictures/4_%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82_%D0%BF%D0%B0%D1%80%D1%81%D0%B8%D0%BD%D0%B3%D0%B0_%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%BE%D0%B2.PNG" alt="Результат_парсинга_товаров" width="500"/>


**5. С помощью выпадающего списка имеем возможностью выбрать/уточнить товар.**
<img src="https://raw.githubusercontent.com/nikolay-py/product_optimizer/main/pictures/5_%D0%92%D0%BE%D0%B7%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D1%8C_%D1%83%D1%82%D0%BE%D1%87%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F_%D1%82%D0%BE%D0%B2%D0%B0%D1%80%D0%B0.PNG" alt="Возможность_уточнения_товара" width="700"/>

## Установка

Клонируйте репозиторий
```
git clone https://github.com/nikolay-py/product_optimizer.git
```
### Запуск через Докер
1. Запустите в консоли
```
docker-compose up
```
2. Приложение будет доступно через браузер по адресу

http://localhost:5000/

3. Запустите парсинг базы данных продуктов

http://localhost:5000/goods/base

**Цены на товары парсятся с сайта [ОКЕЙ-доставка](https://www.okeydostavka.ru/s)**

Дождитесь, пока спарсятся данные по товарам.\
Примерно через 10 минут вы увидете сообщение\
"Наполнение базы продуктов окончен, можете вернуться на страртовую страницу и загурзить рецепт"

4. Вернитесь по адресу http://localhost:5000/ 
5. Введите url итерсующего рецепта с сайта
https://menunedeli.ru/

### Запуск локально (без Докера)

1. Скопируйте файл .env из .env_example
```
cp .env_example .env
```

Или установите свои данные.

2. Установите вирутальное окружение
```
pip install pipenv
```

3. Создайте виртуальное окружение
```
pipenv shell
```
4. Установите зависимости
```
pipenv install
```
5. Запустите программу
```
flask run
```

6. Приложение будет доступно через браузер по адресу

http://localhost:5000/

7. Запустите парсинг базы данных продуктов

http://localhost:5000/goods/base

**Цены на товары парсятся с сайта [ОКЕЙ-доставка](https://www.okeydostavka.ru/s)**

Дождитесь, пока спарсятся данные по товарам.\
Примерно через 10 минут вы увидете сообщение\
"Наполнение базы продуктов окончен, можете вернуться на страртовую страницу и загурзить рецепт"

8. Вернитесь по адресу http://localhost:5000/ 
9. Введите url итерсующего рецепта с сайта
https://menunedeli.ru/
