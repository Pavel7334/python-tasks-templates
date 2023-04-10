# Напишите рекурсивную функцию вычисления факториала factorial, 
# на вход которой подается целочисленное значение n.
def factorial(number):
    if number == 1:
        return number
    return number * factorial(number - 1)


if __name__ == "__main__":
    n = int(input("Введите значение n "))
    print(factorial(n))
