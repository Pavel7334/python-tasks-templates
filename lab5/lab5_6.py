# Дан словарь my_dict = {1: 10, 'a': 5, 'b': -2}. 
# Удалите из него «'a': 5» и выведите в терминал полученный результат. 
def app(my_dict: dict) -> None:
    popped_value = my_dict.pop('a')
    print(my_dict)


if __name__ == "__main__":
    my_dict = {1: 10, "a": 5, "b": -2}
    app(my_dict)
