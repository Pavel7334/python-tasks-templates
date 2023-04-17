# Напишите функцию closure_list_del, на вход которой подается список 
# целочисленных значений. Используя механизм замыкания верните 
# функцию, принимающую на вход значение n и возвращающую список, 
# в котором удалены все элементы, что без остатка делятся на n. 

def closure_list_del(my_list: list) -> list:
    def helper(num: int):
        return [el for el in my_list if el % num == 0]
    return helper


if __name__ == "__main__":
    x = closure_list_del([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(x(2))
    print(x(3))
