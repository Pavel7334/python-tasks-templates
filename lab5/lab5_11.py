# Дан список my_list1 = [1, 2, 3, 4, 9, 7, 4] и my_list2 = [2, 13, 4, 8, 7, 6]. 
# Напишите программу, формирующую словарь, где в качестве ключей 
# выступают элементы первого списка, а в качестве значений - второго. 
def app(my_list1: list, my_list2: list) -> None:
    thisdict = dict.fromkeys(my_list1)

    for idx, elem in enumerate(my_list2):
        thisdict[my_list1[idx]] = elem

    print(thisdict)


if __name__ == "__main__":
    my_list1 = [1, 2, 3, 4, 9, 7, 4]
    my_list2 = [2, 13, 4, 8, 7, 6, 5]
    app(my_list1, my_list2)
