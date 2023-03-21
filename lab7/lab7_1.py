# На вход программы подается 3 значения: val1, val2, val3. 
# Найдите их сумму и выведите полученный результат в терминал. 
def app():
    result = sum([int(input()) for i in range(3)])
    print(result)


if __name__ == "__main__":
    app()

