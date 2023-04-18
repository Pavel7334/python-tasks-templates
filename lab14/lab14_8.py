# Напишите декоратор check_type, который будет проверять 
# тип подаваемого значения в декорируемую функцию reply_int. 
# Если тип данных int – то осуществляется вызов декорируемой функции, 
# а ее результат умножается на два. В любых других случаях – возвращается None. 
# Функция reply_int возвращает подаваемое на ее вход значения, 
# не совершая с ним никаких преобразований.


def check_type(func):
    def helper(el):
        if isinstance(el, int):
            return func(el * 2)
        return None
    return helper


@check_type
def reply_int(el):
    return el


if __name__ == "__main__":
    print(reply_int(2)) # 4
    print(reply_int("ds")) # None
