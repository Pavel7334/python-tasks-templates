# Дан словарь my_dict = {1: 10, 'a': 5, 'b': '^_^'}. 
# Проверьте существует ли в словаре ключ 'a' и 
# выведите полученный результат в терминал.
def app(my_dict: dict) -> None:
    print('a' in my_dict.keys())


if __name__ == "__main__":
    my_dict = {1: 10, "a": 5, "b": "^_^"}
    app(my_dict)
