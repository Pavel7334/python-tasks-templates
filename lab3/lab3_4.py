# Дан кортеж my_tuple = (1, 2, 5, 6). Добавьте новый элемент 
# со значением 12 на 2-ю позицию и выведите в терминал полученный результат.
def app(my_tuple: tuple) -> None:
    new_tuple = my_tuple[:1] + (12,) + my_tuple[2:]
    print(new_tuple)


if __name__ == "__main__":
    my_tuple = (1, 2, 5, 6)
    app(my_tuple)
