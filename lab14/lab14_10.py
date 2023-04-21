# Напишите декоратор mul_result с целочисленным аргументом N, 
# умножающий результат выполнения декорируемой функции на N и 
# возвращающий полученное значение. В качестве декорируемой 
# напишите функцию add, вычисляющий сумму двух поступающих на ее вход значений.

def mul_result(n: int):
    def new_decorator(func):

        def helper(*args, **kwargs):
            print(*args, **kwargs)
            result = func(*args, **kwargs) * n
            return result

        return helper

    return new_decorator


@mul_result(2)
def add(num1: int, num2: int) -> int:
    return num1 + num2


if __name__ == "__main__":
    print(add(3, 5))  # 16
