# Дан словарь my_dict = {'name': 'Alex', 'age':25, 'salary': 8000}. 
# Сформируйте список кортежей пар «ключ:значение» и 
# выведите в терминал полученный результат. 
# Для решения задачи запрещено использовать циклы.
def app(my_dict: dict) -> None:
    items = my_dict.items()
    my_list = list(items)
    print(my_list)


if __name__ == "__main__":
    my_dict = {"name": "Alex", "age": 25, "salary": 8000}
    app(my_dict)
