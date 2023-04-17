# На вход функции closure_del_str подается строка. 
# Используя механизм замыканий, удалите из строки задаваемый 
# в возвращаемой функции символ и верните полученный результат.

def closure_del_str(my_str: str):
    def helper(num: int):
        new_str = my_str[:num] + my_str[num+1:]
        return new_str
    return helper


if __name__ == "__main__":
    x = closure_del_str("qwerty")
    print(x(2))
    print(x(3))
