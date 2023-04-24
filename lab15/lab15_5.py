# Напишите генераторную функцию my_pow, на вход которой 
# подается целочисленное значение n. На каждом шаге итерации 
# генератор должен возвращать n = n^2. 

def my_pow(n: int) -> list:
    while True:
        n = n ** 2
        yield n


if __name__ == "__main__":
    n = 2
    p = my_pow(n)
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
    print(next(p))
