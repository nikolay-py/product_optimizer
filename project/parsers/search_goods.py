"""Search engine of ingredients in the database with goods."""
from typing import Dict, List, Union

from sqlalchemy.sql.expression import and_

from database import get_db
from project.parsers.models import Good

db = get_db()


def division_word(words: str) -> List[str]:
    """Divide the word in half for inexact search."""
    # Делим слово пополам для неточного поиска
    new_words = []
    for word in words:
        new_length = int(len(word) / 2)
        new_word = word[:new_length]
        new_words.append(new_word)
    return new_words


def phrase_limit(phrase: str) -> List[str]:
    """Increase the number of words in the expression. Maintaining a 3-word standard."""
    # Поддерживаем структуру поиска в 3 слова,
    # чтобы избежать ошибки выхода вне индекса
    phrase = phrase.lower().split()
    if len(phrase) > 2:
        return phrase
    else:
        return phrase + ['', '', '']


def search_for_base(words: List[str], num_rows: int = 3) -> List[Dict[str, Union[str, float]]]:
    """Search words in base."""
    # Основной механизм поиска по базе
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


def save_as_dict(base_object: Good) -> Dict[str, Union[str, float]]:
    """Save as dict."""
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


def limit_result(result_list: List[str], length_list: int) -> List[str]:
    """Limiting the number of results."""
    # Сокращаем список результатов поиска
    new_result = []

    if length_list < len(result_list):
        for i in range(length_list - 1):
            new_result.append(result_list[i])
        return new_result

    return result_list


def get_several_variants(phrase: str) -> List[Dict[str, Union[str, float]]]:
    """The function combines several search engines."""
    # Несколько варинатнтов поиска в одной функции
    goods_list = []
    unique_list = []
    words = phrase_limit(phrase)

    # Поиск всех слов
    goods_list += (search_for_base(words))

    # Поиск всех слов по половине слова
    goods_list += (search_for_base(division_word(words)))

    # Поиск каждого слова отдельно
    for i in range(3):
        alone_word = [words[i]] + ['', '']
        goods_list += search_for_base(alone_word)

    # Чистим от поврорящихся результатов поиска
    for good in goods_list:
        if good not in unique_list:
            unique_list.append(good)

    return unique_list
