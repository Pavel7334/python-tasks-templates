# Напишите генераторную функцию list_pow, на вход которой 
# подается список целочисленных значений, и она возвращает 
# на каждой итерации квадрат значения элемента списка.

def list_pow(my_list: int) -> list:
    for el in my_list:
        yield el ** 2


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in list_pow(my_list):
        print(i)
