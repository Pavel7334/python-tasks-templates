# Дан словарь my_dict = {'name': 'Alex', 'age':25, 'salary': 8000}. 
# Измените имя ключа с 'age' на 'years' и выведите в терминал полученный результат.
def app(my_dict: dict) -> None:
    my_dict['years'] = my_dict.pop('age')
    print(my_dict)



if __name__ == "__main__":
    my_dict = {"name": "Alex", "age": 25, "salary": 8000}
    app(my_dict)
