# Дан кортеж my_ tuple = (1, 2, 3, 4, 5, 1, 2, 'a', 'b', 2, 5). 
# Получите номер индекса элемента со значением 'a' и 
# выведите в терминал полученный результат. 
# Для решения задачи запрещено использовать циклы.
def app(my_tuple: tuple) -> None:
    print(my_tuple.index('a'))


if __name__ == "__main__":
    my_tuple = (1, 2, 3, 4, 5, 6, 1, 2, "a", "b", 2, 5)
    app(my_tuple)
