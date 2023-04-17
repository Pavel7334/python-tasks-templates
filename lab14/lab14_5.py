# Напишите декоратор str_case_result, который будет переводить 
# все символы с левой строки результирующего значения функции 
# del_str в верхний регистр, правой стороны – в нижний, а центральный 
# (средний) символ оставлять без изменения. 
# На вход функции del_str подается строка и символ, который из нее надо удалить.


def str_case_result(func):
    def wrapper(my_str, el):
        new_str = my_str[:2].upper() + my_str[len(my_str) // 2 - 1] + my_str[-2:].lower()
        return func(new_str, el)

    return wrapper


@str_case_result
def del_str(my_str: str, el) -> str:
    res_str = my_str.replace(el, '')
    return res_str


if __name__ == "__main__":
    print(del_str("qwerty", "r"))  # QWety
