# Напишите функцию is_anagram, на вход которой подается две строки. 
# Функция должна осуществлять проверку, являются ли переданные 
# значения анаграммами или нет, после чего вернуть 
# результат проверки (True – да, нет – False).
def is_anagram(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()

    position = 0
    matches = True

    while position < len(str1) and matches:
        if list1[position] == list2[position]:
            position = position + 1
        else:
            matches = False

    return matches


if __name__ == "__main__":
    my_str1 = input("Введите первую строку ")
    my_str2 = input("Введите вторую строку ")

    print(is_anagram(my_str1, my_str2))
