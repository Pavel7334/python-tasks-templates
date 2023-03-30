# На вход подается список my_list. Используя списковое включение 
# возведите все его элементы в квадрат и выведите полученный 
# результат в терминал.
def app():
    my_list = list(map(int, input().strip().split()))
    print([el ** 2 for el in my_list])


if __name__ == "__main__":
    app()
