# Дан кортеж my_tuple = (1, 2, 5, 6). 
# Измените значение его элемента 5 на 'b' и выведите в терминал полученный результат.
def app(my_tuple: tuple) -> None:
    my_tuple[5] = 'b'
    print(my_tuple)


if __name__ == "__main__":
    my_tuple = (1, 2, 5, 6)
    app(my_tuple)
