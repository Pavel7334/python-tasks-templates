# Напишите декоратор time_run, вычисляющий время выполнения 
# декорируемой функции и возвращающий время выполнения вместо 
# результата декорируемой функции. 
# В качестве декорируемой напишите функцию algebraic_sum, 
# на вход которой подается два значения N и k (по умолчанию равно 2). 
# Функция должна возвращать результат следующего выражения: 1^k + 2^k + 3^k + … + N^k.
import time


def time_run(func):
    def helper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        return time.time() - start
    return helper


@time_run
def algebraic_sum(n: int = 2, k: int = 2) -> list:
    return sum(num ** k for num in range(1, n + 1))


if __name__ == "__main__":
    number = 500000
    print(f"{algebraic_sum(number):.4f}") # 0.0345
