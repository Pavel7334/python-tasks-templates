# Дан словарь my_dict = {1: 10, 'a': 5, 'b': -2}. 
# Измените значение, хранящееся по ключу 'a' на 10 и 
# выведите в терминал полученный результат. 
def app(my_dict: dict) -> None:
    my_dict['a'] = 10
    print(my_dict)


if __name__ == "__main__":
    my_dict = {1: 10, "a": 5, "b": -2}
    app(my_dict)
