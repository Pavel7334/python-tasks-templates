# Дан список my_list = ['a', 'b', 2, 5], 
# добавьте в него список [3, 't'] и 
# выведите в терминал полученный результат.
from typing import Any


def app(my_list: list[Any]) -> None:
    print(my_list + [3, 't'])


if __name__ == "__main__":
    my_list = ["a", "b", 2, 5]
    app(my_list)
