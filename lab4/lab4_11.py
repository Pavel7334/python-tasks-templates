# Дан список my_list = [1, 0, 1, 10, 5, 6, 7, 4, 4, 1, 6, 2, 5]. 
# Сформируйте новый список, содержащий не повторяющиеся элементы, 
# и выведите его в терминал.
def app(my_list: list) -> None:
    new_list = list(set(my_list))
    print(new_list)


if __name__ == "__main__":
    my_list = [1, 0, 1, 10, 5, 6, 7, 4, 4, 1, 6, 2, 5]
    app(my_list)
