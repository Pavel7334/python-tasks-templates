# Напишите рекурсивную функцию recursion_sum, на вход которой 
# подается целочисленное значение n. Необходимо вычислить 
# сумму всех чисел от 1 до n.

def recursion_sum(num: int) -> int:
    return num + recursion_sum(num-1) if num else 0


if __name__ == "__main__":
    val1 = int(input("Введите значение n "))
    print(recursion_sum(val1))
