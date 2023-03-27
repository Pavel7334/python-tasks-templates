# На вход подается список my_list. Используя цикл for 
# найдите среднеарифметическое значение списка и выведите 
# полученный результат в терминал.
import numpy


def app():
    lst_avg = numpy.average(list(map(int, input().strip().split())))
    print(lst_avg)



if __name__ == "__main__":
    app()
