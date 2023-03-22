# На вход программы подается 3 значения: val1, val2, val3. 
# Вычислите следующее выражение (val1 + val2) / (val2 – val3) 
# и выведите полученный результат в терминал.
def app():
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())
    print((val1 + val2) / (val2 - val3))


if __name__ == "__main__":
    app()
