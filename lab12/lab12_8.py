# Напишите рекурсивную функцию remove_v, 
# удаляющую из строки все заданные буквы и возвращающую 
# результирующую строку.

def remove_v(my_str: str, el: str) -> str:
    # new_1 = ''
    # count = 0
    # for i in my_str:
    #     if i != el:
    #         new_1 += i

    # while count < len(my_str):
    #     if my_str[count] != el:
    #         new_1 += my_str[count]
    #     count += 1

    if not my_str:
        return ''
    if my_str[0] == el:
        result = remove_v(my_str[1:], el)
        return result
    result = my_str[0] + remove_v(my_str[1:], el)
    return result


if __name__ == "__main__":
    my_str = "Приуууувет"
    print(remove_v(my_str, 'у'))
