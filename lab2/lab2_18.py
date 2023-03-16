# Дан список. Используя срезы сформируйте новый список, 
# в состав которого входят последние 5 элементов списка my_list. 
# Выведите в терминал полученный результат.
from typing import Any


def app(my_list: list[Any]) -> None:
    print(my_list + my_list[-5:])


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 2, 3, 2, 1, 2, "a", "b", 2, 5]
    app(my_list)
