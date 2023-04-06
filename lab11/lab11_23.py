# Напишите функцию brackets, которой на вход подается текст 
# (строка), содержащий символы скобок. Функция должна 
# посчитать баланс открывающих и закрывающих скобок и 
# если он соблюден, то вернуть значение – True, 
# иначе – False. Когда в строке отсутствуют скобки должно возвращаться True.
def bracket(string: str) -> bool:

    while '()' in string:
        string = string.replace('()', '')
    return string == ''





if __name__ == "__main__":
    my_str = input("Введите строку со скобками ")

    print(bracket(my_str))


def check_string(string: str) -> bool:
    stack = []
    for s in string:
        if s == ')' and not stack:
            return False
        if s == '(':
            stack.append(s)
        elif s == ')':
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0


print(check_string('(((())'))


def check_string(string: str) -> bool:
    flag = 0
    for s in string:
        if s == ')' and flag == 0:
            return False
        if s == '(':
            flag += 1
        elif s == ')':
            flag -= 1
        if flag < 0:
            return False
    return flag == 0


print(check_string('(()))'))