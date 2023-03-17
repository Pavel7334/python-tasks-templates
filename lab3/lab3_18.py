# Дан кортеж my_ tuple = (1, 2, 3, 4, 'a', 'b', 2, 5). 
# Используя модуль randome извлеките случайный элемент кортежа и 
# выведите в терминал полученный результат. 
# Для решения задачи запрещено использовать циклы.
import random


def app(my_tuple: tuple) -> None:
    print(random.choice(my_tuple))


if __name__ == "__main__":
    my_tuple = (1, 2, 3, 4, "a", "b", 2, 5)
    app(my_tuple)
