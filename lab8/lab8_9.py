# Пользователь вводит с клавиатуры 2 значения (x и y). 
# Определите в какой четверти находится точка с полученной 
# координатой и выведите ее в терминал (1, 2, 3, 4 
# или «Центр координат», «Ось X» (если y = 0) и 
# «Ось Y» (если х=0)). Текст выводить без кавычек!
def app():
    print("Координаты точки:")
    x = float(input("x = "))
    y = float(input("y = "))
    if x > 0 and y > 0:
        print("Точка в 1 четверти")
    elif x < 0 and y > 0:
        print("Точка во 2 четверти")
    elif x < 0 and y < 0:
        print("Точка в 3 четверти")
    elif x > 0 and y < 0:
        print("Точка в 4 четверти")
    elif x == 0 and y == 0:
        print("Точка в центре координат")
    elif x == 0:
        print("Точка на оси X")
    elif y == 0:
        print("Точка на оси Y")


if __name__ == "__main__":
    app()
