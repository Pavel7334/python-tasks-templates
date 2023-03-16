# Дан кортеж my_tuple = (1, 2, 3, 10). Удалите у него элемент 
# со значением 3 и выведите в терминал полученный результат.
def app(my_tuple: tuple) -> None:
    new_list = list(my_tuple)
    new_list.remove(3)
    print(new_list)


if __name__ == "__main__":
    my_tuple = (1, 2, 3, 10)
    app(my_tuple)
