# Дан словарь my_dict = {'name': 'Alex', 'age':25, 'salary': 8000}. 
# Сформируйте список  из значений словаря и выведите в 
# терминал полученный результат. 
# Для решения задачи запрещено использовать циклы.
def app(my_dict: dict) -> None:
    print(list(my_dict.values()))
 

if __name__ == "__main__":
    my_dict = {"name": "Alex", "age": 25, "salary": 8000}
    app(my_dict)
