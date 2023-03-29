# На вход программы подается 2 значения: val1, val2. 
# Используя списковое включение создайте список длинной val1, 
# проинициализированный значениями val2 и выведите полученный результат в терминал.
def app():
    val1 = int(input())
    val2 = int(input())
    new_list = [val2 for _ in range(val1)]
    print(new_list)


if __name__ == "__main__":
    app()
