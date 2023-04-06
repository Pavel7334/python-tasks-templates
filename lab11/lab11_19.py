# Напишите функцию lmc, на вход которой подается два целочисленных значения. 
# Функция должна быть реализована без использования рекурсии и 
# возвращать их наименьшее общее кратное.
def lmc(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
    return lcm


if __name__ == "__main__":
    my_val1 = int(input("Введите первое значение "))
    my_val2 = int(input("Введите второе значение "))

    print(lmc(my_val1, my_val2))
