# Напишите функцию is_palindrome, которая проверяет является 
# ли подаваемая на ее вход строка палиндромом и возвращает 
# значение булевского типа данных (True – да, нет – False).
def is_palindrome(val):
    return val == val[::-1]


if __name__ == "__main__":
    my_str = input("Введите строку ")

    print(is_palindrome(my_str))
