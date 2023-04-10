# Напишите рекурсивную функцию pow_n, на вход которой 
# подается два значения n и k (по умолчанию равно 8). 
# Функция должна возвращать значение следующего вида: n^k.

def pow_n(n: int, k: int = 8) -> int:
    # meaning = 1
    # while k > 0:
    #     meaning *= n
    #     k -= 1
    # return meaning
    if k == 0:
        return 1
    return n * pow_n(n, k - 1)


if __name__ == "__main__":
    n = int(input("Введите значение n "))
    print(pow_n(n))
