# Напишите рекурсивную функцию recursion_palindrom, на вход которой 
# подается строка. Если строка представляет собой палиндром, 
# то функция должна вернуть значение – True, иначе – False.

def recursion_palindrom(my_str: str) -> bool:
    if my_str[0] != my_str[-1]:
        return False
    if len(my_str) > 2:
        return recursion_palindrom(my_str[1:-1])
    return True


if __name__ == "__main__":
    my_strt = "11145111"
    print(recursion_palindrom(my_strt))
