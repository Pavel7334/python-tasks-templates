# Напишите функцию closure_list_pow, на вход которой подается 
# список целочисленных или вещественных значений. Используя 
# механизм замыкания верните функцию, принимающую значение степени, 
# в которую необходимо возвести каждый элемент списка и возвращающую 
# полученный результат.

def closure_list_pow(my_list: list) -> list:
    def helper(num: int):
        return [el ** num for el in my_list]
    return helper


if __name__ == "__main__":
    x = closure_list_pow([1, 2.5, 3, 7, 5.25])
    print(x(0))
    print(x(1))
    print(x(2))
