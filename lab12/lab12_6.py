# Напишите рекурсивную функцию вычисления числа Фибоначчи fibonacci, 
# на вход которой подается целочисленное значение n.

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    n = int(input("Введите значение n "))
    print(fibonacci(n))
