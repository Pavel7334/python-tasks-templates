# Напишите декоратор sqrt_list_result, который будет вычислять корень 
# результирующего значения функции max_number, на вход которой 
# подается целочисленный список и возвращается его найденное максимальное значение.
from math import sqrt


def sqrt_list_result(func):
    def wrapper(my_list):
        return sqrt(func(my_list))
    return wrapper


@sqrt_list_result
def max_number(my_list: list) -> int:
    return max(my_list)


if __name__ == "__main__":
    my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(max_number(my_list1))  # 3.0
