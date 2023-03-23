# Напишите программу, выводящую в терминал «YES» или «NO» 
# (без кавычек) в зависимости от того, какой год пользователь 
# ввел с клавиатуры (високосный или нет).
import calendar


def app():
    year = int(input('Введите год: '))

    if year % 4 != 0:
        print('NO')

    elif year % 100 == 0:
        if year % 400 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('YES')


if __name__ == "__main__":
    app()
