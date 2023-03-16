# Инвертируйте (переверните) список my_list = [1, 2, 3, 4, 5, 6, 2, 3, 2, 1, 2, 'a', 'b', 2, 5]
# и выведите в терминал полученный результат.
from typing import Any


def app(my_list: list[Any]) -> None:
    print(my_list[::-1])


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 2, 3, 2, 1, 2, "a", "b", 2, 5]
    app(my_list)
