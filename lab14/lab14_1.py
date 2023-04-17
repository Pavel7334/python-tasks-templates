# Напишите декоратор pow_list_result, который будет возводить в квадрат 
# результирующее значение (элементы списка) функции sum_list, 
# на вход которой подается целочисленный список и возвращается сумма его элементов.

def pow_list_result(func):
    def wrapper(my_list):
        return func(my_list) ** 2
    return wrapper


@pow_list_result
def sum_list(my_list1):
    return sum(my_list1)


if __name__ == "__main__":
    my_list1 = [2, 2, 2, 4]
    print(sum_list(my_list1))  # 100
