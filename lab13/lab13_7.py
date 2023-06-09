# Напишите функцию closure_count_str, на вход которой подается строка.
# Функция должна возвращать другую функцию, принимающую символ 
# и возвращающую количество его повторений. 

def closure_count_str(my_str: str) -> int:
    def helper(el: str):
        new_str = my_str.count(el)
        return new_str
    return helper


if __name__ == "__main__":
    x = closure_count_str("qwerqqrqqqqtqqry")
    print(x("q"))
    print(x("r"))
