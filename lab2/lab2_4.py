# Дан список my_list = [1, 2, 3, 10]. 
# Вставьте новый элемент со значением 12 на 2-ю позицию и 
# выведите в терминал полученный результат.

def app(my_list: list[int]) -> None:
    my_list[1] = 12
    print(my_list)


if __name__ == "__main__":
    my_list = [1, 2, 3, 10]
    app(my_list)
