# Дан кортеж my_ tuple = (1, 2, 3, 4, 5, 6, 2, 3, 2, 1, 2, 'a', 'b', 2, 5). 
# Используя срезы сформируйте новый кортеж, в состав которого входят элементы, 
# начиная с 0-го индекса по 4-й. Выведите в терминал полученный результат.
def app(my_tuple: tuple) -> None:
    print(my_tuple[:4])


if __name__ == "__main__":
    my_tuple = (1, 2, 3, 4, 5, 6, 1, 2, "a", "b", 2, 5)
    app(my_tuple)
