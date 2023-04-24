# Напишите генераторную функцию list_odd, на вход которой 
# подается список целочисленных значений. Функция должна возвращать 
# только четные значения из поданного на ее вход списка.

def list_odd(my_list: list) -> list:
    for num in my_list:
        if num % 2 == 0:
            yield num


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 6, 4, 7, 8, 9]

    for i in list_odd(my_list):
        print(i)
