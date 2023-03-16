# Дан список my_list = [1, 2, 3, 10]. Удалите элемент со значением 3 
# и выведите в терминал полученный результат.

def app(my_list: list[int]) -> None:
    my_list.remove(3)
    print(my_list)


if __name__ == "__main__":
    my_list = [1, 2, 3, 10]
    app(my_list)
