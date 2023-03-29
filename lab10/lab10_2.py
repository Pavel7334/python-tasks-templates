# На вход подается список my_list. Используя списковое включение, 
# удалите из него все элементы, которые нацело делятся на 2 и 
# выведите полученный результат в терминал.
def app():
    my_list = list(map(int, input().strip().split()))
    print([el for el in my_list if el % 2 != 0])


if __name__ == "__main__":
    app()
