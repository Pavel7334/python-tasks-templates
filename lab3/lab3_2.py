# Распакуйте кортеж my_tuple = (1, 6) в переменные value1 и value2. 
# Выведите в терминал полученный результат через пробел - 1 6.
def app(my_tuple: tuple) -> None:
    value1, value2 = my_tuple
    print(value1, value2)


if __name__ == "__main__":
    my_tuple = (1, 6)
    app(my_tuple)
