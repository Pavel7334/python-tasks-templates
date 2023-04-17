# Напишите декоратор upcase_result, который будет переводить 
# все символы результирующего значения функции reverse_str 
# в верхний регистр. На вход функции reverse_str подается 
# строка и возвращается ее инвертированное представление.


def upcase_result(func):
    def wrapper(my_str):
        return func(my_str).upper()

    return wrapper


@upcase_result
def reverse_str(my_str: str) -> str:
    return my_str[::-1]


if __name__ == "__main__":
    my_str1 = "qwerty"
    print(reverse_str(my_str1))  # YTREWQ
