# Напишите функцию count_uppercase, на вход которой 
# подается строка с буквами в различном регистре. 
# Функция должна возвращать количество прописных букв.
def count_uppercase(my_str):
    return len([letter for letter in my_str if letter.isupper()])


if __name__ == "__main__":
    my_str = input("Введите искомое значение ")

    print(count_uppercase(my_str))
