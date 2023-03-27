# На вход подается список my_list. Используя цикл for 
# найдите среднеарифметическое значение списка и выведите 
# полученный результат в терминал.
import numpy


def app():
    my_list = list(map(int, input().strip().split())) # Первый вариант
    lst_avg = numpy.average(list(map(int, input().strip().split()))) # Второй вариант
    print(lst_avg)
    print(sum(my_list) / len(my_list))


if __name__ == "__main__":
    app()
