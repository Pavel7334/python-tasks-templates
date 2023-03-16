# Дан кортеж my_tuple = (1, 2, 5, 6). 
# Измените значение его элемента 5 на 'b' и выведите в терминал полученный результат.
def app(my_tuple: tuple) -> None:
    a, b, c, d = my_tuple
    с = 'b'
    print(a, b, с, d)


if __name__ == "__main__":
    my_tuple = (1, 2, 5, 6)
    app(my_tuple)
