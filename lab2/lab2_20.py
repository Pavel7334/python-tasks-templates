# Дан список. Используя модуль randome извлеките случайный элемент списка и 
# выведите в терминал полученный результат. 
# Для решения задачи запрещено использовать циклы. 
from typing import Any
import random


def app(my_list: list[Any]) -> None:
    print(random.choice(my_list))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 2, 3, 2, 1, 2, "a", "b", 2, 5]
    app(my_list)
