# procedural.py - процедуры обработки процедурного языка
import random
from language import Language


class Procedural(Language):
    def __init__(self):
        super().__init__()
        # присутствие абстрактных типов данных
        self.is_abstract = False

    # ввод параметров процедурного языка из файла
    def read_params(self, str_array, position):
        # должно оставаться 4+ непрочитанных значений
        if position >= len(str_array) - 3:
            return 0
        # считываем название
        self.name = str_array[position]
        # считываем популярность
        self.popularity = float(str_array[position + 1])
        # считываем год
        self.year = int(str_array[position + 2])
        # считываем присутствие абстрактных типов данных
        self.is_abstract = bool(str_array[position + 3])
        position += 4

        if self.year < 1945 or self.year > 2022 or self.popularity < 0 or self.popularity > 100:
            print("Incorrect PROCEDURAL. It will be randomly generated.")
            self.generate_params()

        return position

    # генерация параметров процедурного языка
    def generate_params(self):
        name_len = random.randint(1, 40)
        letters = 'abcdefghijklmnopqrstuvwxyz'
        self.name = ''.join(random.choice(letters) for i in range(name_len))
        self.year = random.randint(1945, 2022)
        self.popularity = random.random() * 100
        self.is_abstract = random.randint(0, 1)
        pass

    # вывод процедурного языка в консоль
    def print(self):
        print(
            "PROCEDURAL."
            "Name: {},\n"
            "Popularity: {},\n"
            "Year = {},\n"
            "Has abstract data types: {}.\n"
            "Parameter value: {}.\n\n".format(
                self.name, self.popularity, self.year, self.is_abstract, self.get_parameter()))
        pass

    # вывод процедурного языка в указанный поток
    def write(self, output_stream):
        output_stream.write(
            "PROCEDURAL."
            "Name: {},\n"
            "Popularity: {},\n"
            "Year = {},\n"
            "Has abstract data types: {}.\n"
            "Parameter value: {}.\n".format(
                self.name, self.popularity, self.year, self.is_abstract, self.get_parameter()))
        pass
