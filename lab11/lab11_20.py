# Напишите функцию gcd, на вход которой подается два целочисленных значения. 
# Функция должна быть реализована без использования рекурсии и 
# возвращать их наибольший общий делитель.

def gcd(val1, val2):
    common = 0
    if val1 > val2:
        temp = val2
    else:
        temp = val1
    for i in range(1, temp + 1):
        if val1 % i == 0 and val2 % i == 0:
            common = i
    return common


if __name__ == "__main__":
    my_val1 = int(input("Введите первое значение "))
    my_val2 = int(input("Введите второе значение "))

    print(gcd(my_val1, my_val2))
