# На вход программы подается 2 значения: val1, val2. 
# Если val1 делится на val2 без остатка, то выведите 
# в терминал «Bingo!» (без кавычек), иначе выведите 
# получившийся остаток от деления.
def app():
    val1 = int(input())
    val2 = int(input())
    if val1 % val2 == 0:
        print('Bingo!')
    else:
        print(val1 % val2)


if __name__ == "__main__":
    app()
