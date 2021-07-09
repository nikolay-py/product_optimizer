from sqlalchemy.sql.expression import and_
from database import get_db
from project.parsers.models import Good

db = get_db()


# Делим слово пополам для неточного поиска
def division_word(words):
    new_words = []
    for word in words:
        new_length = int(len(word) / 2)
        new_word = word[:new_length]
        new_words.append(new_word)
    return new_words


# Поддерживаем структуру поиска в 3 слова,
# чтобы избежать ошибки выхода вне индекса
def phrase_limit(phrase):
    phrase = phrase.lower().split()
    if len(phrase) > 2:
        return phrase
    else:
        return phrase + ['', '', '']


# Основной механизм поиска по базе
def search_for_base(words, num_rows=3):
    result_search = []
    top_good = db.query(Good).filter(
        and_(
            Good.name.ilike(f'%{words[0]}%'),
            Good.name.ilike(f'%{words[1]}%'),
            Good.name.ilike(f'%{words[2]}%'),
        )
    ) \
        .order_by(Good.price_per_kg.asc()) \
        .limit(num_rows)

    for good in top_good:
        result_search.append(save_as_dict(good))

    return result_search


def save_as_dict(base_object):
    base_object = {
        'id': base_object.id,
        'key': base_object.category,
        'name': base_object.name,
        'price': base_object.price,
        'weight': base_object.weight,
        'units': base_object.units,
        'price_per_kg': base_object.price_per_kg
    }
    return base_object


# Сокращаем результат выдачи
def limit_result(result_list, length_list):
    new_result = []

    if length_list < len(result_list):
        for i in range(length_list - 1):
            new_result.append(result_list[i])
        new_result.append({'name': 'товар не найден'})
        return new_result

    result_list.append({'name': 'товар не найден'})
    return result_list


# Несколько варинатнтов поиска в одной функции
def get_product(phrase, length_list=10):
    goods_list = []
    unique_list = []
    words = phrase_limit(phrase)

    # Поиск всех слов
    goods_list += (search_for_base(words))

    # Поиск всех слов по половине слова
    goods_list += (search_for_base(division_word(words)))

    # Поиска каждого слова отдельно
    for i in range(3):
        alone_word = [words[i]] + ['', '']
        goods_list += search_for_base(alone_word)

    # Чистим от поврорящихся результатов поиска
    for good in goods_list:
        if good not in unique_list:
            unique_list.append(good)

    # Ставим ограничение на выдачу результатов
    limited_unique_list = limit_result(unique_list,length_list)

    return limited_unique_list


# if __name__ == '__main__':
#     get_product('Филе бедра индейки охлажденное ТЧН (ОКЕЙ DAILY), кг')
