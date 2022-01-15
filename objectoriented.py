# objectoriented.py - процедуры обработки объектно-ориентированного языка
import random
from language import Language


class Objectoriented(Language):
    def __init__(self):
        super().__init__()
        # наследование
        self.inheritance = ""

    # ввод параметров объектно-ориентированного языка из файла
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
        # считываем ключ для наследования и выводим тип наследования
        key = int(str_array[position + 3])
        if key == 0:
            self.inheritance = "single"
        elif key == 1:
            self.inheritance = "multiple"
        elif key == 2:
            self.inheritance = "interface"
        position += 4

        if self.year < 1945 or self.year > 2022 or self.popularity < 0 or self.popularity > 100 or self.inheritance == "":
            print("Incorrect OBJECTORIENTED. It will be randomly generated.")
            self.generate_params()

        return position

    # генерация параметров объектно-ориентированного языка
    def generate_params(self):
        name_len = random.randint(1, 40)
        letters = 'abcdefghijklmnopqrstuvwxyz'
        self.name = ''.join(random.choice(letters) for i in range(name_len))
        self.year = random.randint(1945, 2022)
        self.popularity = random.random() * 100
        key = random.randint(0, 2)
        if key == 0:
            self.inheritance = "single"
        elif key == 1:
            self.inheritance = "multiple"
        else:
            self.inheritance = "interface"
        pass

    # вывод объектно-ориентированного языка в консоль
    def print(self):
        print(
            "OBJECTORIENTED.\n"
            "Name: {},\n"
            "Popularity: {},\n"
            "Year = {},\n"
            "Inheritance: {}.\n"
            "Parameter value: {}.\n\n".format(
                self.name, self.popularity, self.year, self.inheritance, self.get_parameter()))
        pass

    # вывод объектно-ориентированного языка в указанный поток
    def write(self, output_stream):
        output_stream.write(
            "OBJECTORIENTED.\n"
            "Name: {},\n"
            "Popularity: {},\n"
            "Year = {},\n"
            "Inheritance: {}.\n"
            "Parameter value: {}.\n".format(
                self.name, self.popularity, self.year, self.inheritance, self.get_parameter()))
        pass
