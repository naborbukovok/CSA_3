# utils.py - функции обработки и генерации данных
import random

from functional import Functional
from objectoriented import Objectoriented
from procedural import Procedural


# обработка ввода языков
def read_data(container, input_data):
    data_count = len(input_data)
    if data_count < 5:
        return 0

    # позиция обрабатываемого элемента
    position = 0
    # количество считанных языков
    language_count = 0
    while position < data_count:
        key = input_data[position]
        if key == "1":
            language = Functional()
        elif key == "2":
            language = Objectoriented()
        elif key == "3":
            language = Procedural()
        else:
            print(position)
            # ошибка чтения языка: возвращаем число уже прочитанных
            return language_count

        position += 1
        # дошли до конца данных: возвращаем число прочитанных языков
        if position == data_count:
            return language_count

        # чтение параметров языка
        position = language.read_params(input_data, position)
        if position == 0:
            return language_count
        language_count += 1
        container.data.append(language)
    return language_count


# генерация языка
def generate_language():
    key = random.randint(0, 2)
    if key == 1:
        language = Functional()
    elif key == 2:
        language = Objectoriented()
    else:
        language = Procedural()
    language.generate_params()
    return language
