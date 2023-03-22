# На вход программы подается 2 значения: val1, val2. 
# Если их произведение больше 400, то в терминал 
# выводится получаемое значение, иначе выведите их сумму.
def app():
    val1 = int(input())
    val2 = int(input())
    if val1 * val2 > 400:
        print(val1 * val2)
    else:
        print(val1 + val2)


if __name__ == "__main__":
    app()
