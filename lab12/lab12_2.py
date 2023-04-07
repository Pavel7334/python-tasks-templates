# Напишите рекурсивную функцию recursion_min, на вход которой 
# подается целочисленный список. Функция должна вернуть значение 
# минимального элемента списка.

def recursion_min(lst: list) -> int:
    if len(lst) == 1:
        return lst[0]

    else:
        return min(lst[0], recursion_min(lst[1:]))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, -6]
    print(recursion_min(my_list))
