# Дан кортеж my_tuple = (1, 2, 5, 6). Выведите в терминал его размер.
def app(my_tuple: tuple) -> None:
    print(len(my_tuple))


if __name__ == "__main__":
    my_tuple = (1, 2, 5, 6)
    app(my_tuple)
