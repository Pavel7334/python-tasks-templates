#Напишите функцию list_create, на вход которой подается 3 значения 
# любого типа и возвращающую сформированный из них список.
from collections.abc import Iterable


def list_create(a, b, c):
    result = []
    for arg in (a, b, c):
        if isinstance(arg, Iterable) and not isinstance(arg, str):
            result.extend(arg)
        else:
            result.append(arg)

    return result


print(list_create([1, 3, 4], 3, 'test'))


# def list_create(a, b, c):                     2-e решение
#     result = []
#     for arg in (a, b, c):
#         if type(arg) == str:
#             result.append(arg)
#             continue
#         try:
#             iter(arg)
#         except TypeError:
#             result.append(arg)
#         else:
#             result.extend(arg)
#
#     return result
#
#
# print(list_create([1, 3, 4], 3, 'test'))


# def list_create(a, b, c):                 3-e решение
#     result = []
#     for arg in (a, b, c):
#         if type(arg) in [list, tuple, set, dict]:
#             result.extend(arg)
#         else:
#             result.append(arg)
#
#     return result
#
#
# print(list_create([1, 3, 4], 3, 'test'))


if __name__ == "__main__":
    my_list1 = [1, 2, 3, 4]
    my_int = 9
    my_str = "test"

    print(list_create(my_list1, my_int, my_str))
