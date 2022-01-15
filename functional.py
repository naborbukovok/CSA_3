# functional.py - процедуры обработки функционального языка
import random
import string
from language import Language


class Functional(Language):
    def __init__(self):
        super().__init__()
        # типизация
        self.type = ""
        # поддержка ленивых вычислений
        self.is_lazy = False

    # ввод параметров функционального языка из файла
    def read_params(self, str_array, position):
        # должно оставаться 5+ непрочитанных значений
        if position >= len(str_array) - 4:
            return 0
        # считываем название
        self.name = str_array[position]
        # считываем популярность
        self.popularity = float(str_array[position + 1])
        # считываем год
        self.year = int(str_array[position + 2])
        # считываем ключ для типа и выводим тип
        key = int(str_array[position + 3])
        if key == 0:
            self.type = "static"
        elif key == 1:
            self.type = "dynamic"
        # считываем поддержку ленивых вычислений
        self.is_lazy = bool(str_array[position + 4])
        position += 5

        if self.year < 1945 or self.year > 2022 or self.popularity < 0 or self.popularity > 100 or self.type == "":
            print("Incorrect FUNCTIONAL. It will be randomly generated.")
            self.generate_params()

        return position

    # генерация параметров функционального языка
    def generate_params(self):
        name_len = random.randint(1, 40)
        letters = 'abcdefghijklmnopqrstuvwxyz'
        self.name = ''.join(random.choice(letters) for i in range(name_len))
        self.year = random.randint(1945, 2022)
        self.popularity = random.random() * 100
        key = random.randint(0, 1)
        if key == 0:
            self.type = "static"
        else:
            self.type = "dynamic"
        self.is_lazy = random.randint(0, 1)
        pass

    # вывод функционального языка в консоль
    def print(self):
        print(
            "FUNCTIONAL.\n"
            "Name: {},\n"
            "Popularity: {},\n"
            "Year = {},\n"
            "Type: {},\n"
            "Supports lazy evaluation: {}.\n"
            "Parameter value: {}.\n\n".format(
                self.name, self.popularity, self.year, self.type, self.is_lazy, self.get_parameter()))
        pass

    # вывод функционального языка в указанный поток
    def write(self, output_stream):
        output_stream.write(
            "FUNCTIONAL.\n"
            "Name: {},\n"
            "Popularity: {},\n"
            "Year = {},\n"
            "Type: {},\n"
            "Supports lazy evaluation: {}.\n"
            "Parameter value: {}.\n".format(
                self.name, self.popularity, self.year, self.type, self.is_lazy, self.get_parameter()))
        pass
