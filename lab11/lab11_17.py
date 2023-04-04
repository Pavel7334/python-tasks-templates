# Напишите функцию count_uppercase, на вход которой 
# подается строка с буквами в различном регистре. 
# Функция должна возвращать количество прописных букв.
def count_uppercase(my_str):
    return len("".join([l for l in my_str if l.isupper()]))
    # count1 = 0
    #
    # for el in my_str:
    #     if el.isupper() == True:
    #         count1 += 1
    #
    # return "Колличество прописных букв", count1


if __name__ == "__main__":
    my_str = input("Введите искомое значение ")

    print(count_uppercase(my_str))
