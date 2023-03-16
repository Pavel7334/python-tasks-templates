# Дан список. Получите номер индекса элемента со значением 'a' и 
# выведите в терминал полученный результат. 
# Для решения задачи запрещено использовать циклы.
from typing import Any


def app(my_list: list[Any]) -> None:
    print(my_list.index('a'))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 2, 3, 2, 1, 2, "a", "b", 2, 5]
    app(my_list)
