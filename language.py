# language.py - процедуры обработки и создания языка
class Language:

    def __init__(self):
        self.name = ""
        self.popularity = 0
        self.year = 0

    # ввод параметров языка
    def read_params(self, str_array, position):
        pass

    # генерация параметров языка
    def generate_params(self):
        pass

    # вывод языка в консоль
    def print(self):
        pass

    # вывод языка в указанный поток
    def write(self, output_stream):
        pass

    # вычисление заданного параметра
    def get_parameter(self):
        return self.year / len(self.name)
