# Напишите рекурсивную функцию recursion_max, на вход которой 
# подается целочисленный список. Функция должна вернуть значение 
# максимального элемента списка. 

def recursion_max(lst: list) -> int:
    if len(lst) == 1:
        return lst[0]

    else:
        return max(lst[0], recursion_max(lst[1:]))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, -6]
    print(recursion_max(my_list))
