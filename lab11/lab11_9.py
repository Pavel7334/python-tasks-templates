# Напишите функцию list_create, на вход которой подается 
# 3 значения целочисленного типа данных. Первые два аргумента 
# задают диапазон значений, которые будут добавлены в формируемый 
# список, а третий аргумент отвечает за шаг. 
# После завершения работы функция должна вернуть созданный список.

def list_create(start, stop, step):
    new_list = []
    for i in range(start, stop, step):
        new_list.append(i)
    return new_list


if __name__ == "__main__":
    start = int(input("Введите начальное значение "))
    stop = int(input("Введите конечное значение "))
    step = int(input("Введите шаг "))

    print(list_create(start, stop, step))
