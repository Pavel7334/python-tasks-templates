# Дан кортеж my_tuple = (1, 2, 5, 6, 7, 6, 2, 5). 
# На его основе сформируйте множество my_set и 
# выведите в терминал полученный результат.
def app(my_tuple: tuple) -> None:
    my_set = set(my_tuple)
    print(my_set)


if __name__ == "__main__":
    my_tuple = (1, 2, 5, 6, 7, 6, 2, 5)
    app(my_tuple)
