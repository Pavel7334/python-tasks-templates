# Напишите функцию sum_n, на вход которой подается 
# целочисленное значение n. Функция должна возвращать 
# сумму значений от нуля до n-1.
def sum_n(val):
    return sum(range(val))


if __name__ == "__main__":
    my_var1 = int(input("Введите значение "))

    print(sum_n(my_var1))
