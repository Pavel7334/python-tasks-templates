# Напишите функцию add, принимающую на вход два списка
# и возвращающую сумму их элементов.
def add(my_list1, my_list2):
    return sum(my_list1 + my_list2)


if __name__ == "__main__":
    my_list1 = list(map(int, input().strip().split()))
    my_list2 = list(map(int, input().strip().split()))

    print(add(my_list1, my_list2))
