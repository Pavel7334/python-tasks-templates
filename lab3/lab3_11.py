# Инвертируйте (переверните) кортеж 
# my_ tuple = (1, 2, 3, 4, 5, 6, 1, 2, 'a', 'b', 2, 5) и 
# выведите в терминал полученный результат.
def app(my_tuple: tuple) -> None:
    new_tup = my_tuple[::-1]
    print(new_tup)


if __name__ == "__main__":
    my_tuple = (1, 2, 3, 4, 5, 6, 1, 2, "a", "b", 2, 5)
    app(my_tuple)
