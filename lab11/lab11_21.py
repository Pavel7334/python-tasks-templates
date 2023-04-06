# Напишите функцию volume_of_box на вход которой подается 3 значения 
# (ширина, длина, высота), где 2 значения (ширина = 10, высота = 7) 
# заданы по умолчанию. Функция должна рассчитывать и 
# возвращать объем коробки с заданными параметрами.
def volume_of_box(val3: int, val1: int = 10, val2: int = 7) -> int:
    return val1 * val2 * val3


if __name__ == "__main__":
    l = int(input("Введите длину "))
    w = int(input("Введите ширину "))
    h = int(input("Введите высоту "))

    print(volume_of_box(l, w, h))
    print(volume_of_box(l))
