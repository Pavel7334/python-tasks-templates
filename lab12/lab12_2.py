# Напишите рекурсивную функцию recursion_min, на вход которой 
# подается целочисленный список. Функция должна вернуть значение 
# минимального элемента списка.

def recursion_min(lst: list) -> int:
    num = 0
    for el in lst:
        if el < num:
            num = el
    return num


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, -6]
    print(recursion_min(my_list))
