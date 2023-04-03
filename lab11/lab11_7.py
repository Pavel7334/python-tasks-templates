# Напишите функцию reverse_str, на вход которой подается строка 
# и возвращается ее инвертированное представление.
def reverse_str(value: str) -> str:
    return value[::-1]


if __name__ == "__main__":
    my_str = input("Введите искомое значение ")

    print(reverse_str(my_str))
