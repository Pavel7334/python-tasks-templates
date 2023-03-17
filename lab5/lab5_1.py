# Дан словарь my_dict = {1: 10, 'a': 5, 'b': '^_^'}. 
# Выведите в терминал количество его элементов.
def app(my_dict: dict) -> None:
    print(len(my_dict))


if __name__ == "__main__":
    my_dict = {1: 10, 'a': 5, 'b': '^_^'}
    app(my_dict)
