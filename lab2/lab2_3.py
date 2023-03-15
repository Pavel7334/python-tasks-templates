# Дан список my_list = [1, 2, 3]. 
# Добавьте в его начало значение 12 и выведите в терминал полученный результат.

def app(my_list: list[int]) -> None:
    my_list.insert(0, 12)
    print(my_list)


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6]
    app(my_list)
