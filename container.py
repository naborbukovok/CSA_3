# container.py - простейший контейнер (тип данных)


class Container:
    # максимальная длина массива
    MAX_LEN = 10000

    def __init__(self):
        # массив языков
        self.data = []
        pass

    # вывод языков в консоль
    def print(self):
        for i in range(len(self.data)):
            print("{}. ".format(i), end='')
            self.data[i].print()
        pass

    # вывод языков в указанный поток
    def write(self, output_stream):
        for i in range(len(self.data)):
            output_stream.write("{}. ".format(i))
            self.data[i].write(output_stream)
            output_stream.write("\n")
        pass

    # функция для изменения порядка согласно условию, возвращает средний параметр по языкам
    def swap_elements(self):
        average_parameter = 0
        for i in range(len(self.data)):
            average_parameter += self.data[i].get_parameter()
        average_parameter /= len(self.data)
        to_begin = []
        to_end = []
        for i in range(len(self.data)):
            if self.data[i].get_parameter() > average_parameter:
                to_end.append(self.data[i])
            else:
                to_begin.append(self.data[i])
        self.data = to_begin + to_end
        pass
