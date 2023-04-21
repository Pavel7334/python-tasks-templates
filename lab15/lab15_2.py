# Напишите генераторную функцию вычисления числа Фибоначчи fibonacci, 
# на вход которой подается целочисленное значение n. 
# Функция не должна использовать рекурсию.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    n = 10
    for i in fibonacci(n):
        print(i)
