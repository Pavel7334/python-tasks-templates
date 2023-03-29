# На вход подается список my_list. Используя списковое включение 
# сформируйте список, элементы которого нацело делятся на 3 и 5 
# и выведите полученный результат в терминал.
def app():
    my_list = list(map(int, input().strip().split()))
    print([el for el in my_list if el % 3 == 0 and el % 5 == 0])


if __name__ == "__main__":
    app()
