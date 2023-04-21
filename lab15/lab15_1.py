# Напишите генераторную функцию my_generator, которая позволяет итерироваться 
# по элементам заданного отрезка с настраиваемым шагом step (по умолчанию равен 1).
# При написании данной функции запрещено использовать стандартную 
# функцию верхнего уровня –  range.

def my_generator(val: int, step: int = 1):

    while val > 0:
        yield val
        val -= step


if __name__ == "__main__":
    my_step = 3
    length = 10
    gen = my_generator(length, my_step)

    for i in gen:
        print(i)
