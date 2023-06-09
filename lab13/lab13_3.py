# Напишите функцию closure_str, на вход которой подается строка. 
# Функция должна возвращать другую функцию, принимающую номер 
# индекса и возвращающую символ, располагаемый в строке по этому 
# индексу. Если задаваемый индекс выходит за пределы строки, 
# то верните пустой символ.

def closure_str(my_str: str):
    def helper(ind: int):
        return my_str[ind] if ind < len(my_str) else ''
    return helper


if __name__ == "__main__":
    my_str1 = "qwerty"
    x = closure_str(my_str1)
    print(x(0))
    print(x(10))
    print(x(2))
