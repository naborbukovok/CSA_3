# main.py - содержит главную функцию, обеспечивающую простое тестирование.
import sys
import time

from container import Container
from utils import read_data, generate_language


def error_message():
    print("Incorrect command line! You must write: python main -f <inputFileName> <outputFileName1> <outputFileName2>")
    print("Or")
    print("Incorrect command line! You must write: python main -n \"number\" <outputFileName1> <outputFileName2>")


if __name__ == '__main__':

    # засекаем время
    start_time = time.time()

    print("Start")

    if len(sys.argv) != 5:
        error_message()
        exit(1)

    # создание контейнера
    container = Container()

    if sys.argv[1] == '-f':
        input_file_name = sys.argv[2]
        output_file_name1 = sys.argv[3]
        output_file_name2 = sys.argv[4]

        # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки.
        input_stream = open(input_file_name)
        input_string = input_stream.read()
        input_stream.close()

        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        input_data = input_string.replace("\n", " ").split(" ")
        language_count = read_data(container, input_data)
        if language_count > Container.MAX_LEN or language_count <= 0:
            print("Incorrect number of languages ({}).".format(language_count, container.MAX_LEN))
            exit(2)

    elif sys.argv[1] == '-n':
        size = int(sys.argv[2])
        output_file_name1 = sys.argv[3]
        output_file_name2 = sys.argv[4]

        if size > Container.MAX_LEN or size <= 0:
            print("Incorrect number of languages ({}).".format(size, container.MAX_LEN))
            exit(2)
        while size != 0:
            container.data.append(generate_language())
            size -= 1
    else:
        error_message()
        exit(1)

    print("There are ", len(container.data), " languages in container:")
    container.print()

    output_stream1 = open(output_file_name1, 'w')
    output_stream1.write("There are {} languages in container:\n".format(len(container.data)))
    container.write(output_stream1)
    output_stream1.close()

    container.swap_elements()

    print("\nSwapped languages:".format(len(container.data)))
    container.print()

    output_stream2 = open(output_file_name2, 'w')
    output_stream2.write("Swapped languages:\n".format(len(container.data)))
    container.write(output_stream2)
    output_stream2.close()

    print("\n%s seconds" % (time.time() - start_time))

    print("Stop")
