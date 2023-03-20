# Дан список my_list1 = [1, 2, 3, 4, 9, 7, 4] и my_list2 = [2, 13, 4, 8, 7, 6]. 
# Напишите программу, формирующую словарь, где в качестве ключей 
# выступают элементы первого списка, а в качестве значений - второго. 
def app(my_list1: list, my_list2: list) -> None:
    new_dict = {}
    for i, sym in enumerate(my_list1):
        new_dict[sym] = new_dict.get(sym, 0) + my_list2[i]
    print(new_dict)


if __name__ == "__main__":
    my_list1 = [1, 2, 3, 4, 9, 7, 4]
    my_list2 = [2, 13, 4, 8, 7, 6, 5]
    app(my_list1, my_list2)
