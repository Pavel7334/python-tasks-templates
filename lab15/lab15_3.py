# Напишите генераторную функцию my_enumerate, 
# на вход которой подается список и она возвращает на каждой 
# итерации кортеж, состоящий из двух элементов: index – 
# текущий номер индекса элемента, val – значение, 
# хранящееся по этому индексу. 
# При написании данной функции запрещено использовать 
# стандартную функцию верхнего уровня – enumerate.

def my_enumerate(my_list: list) -> tuple:
    for i in my_list:
        yield i, my_list.index(i)


if __name__ == "__main__":
    my_list = ["a", "b", "c", "d"]

    for i in my_enumerate(my_list):
        print(i)
