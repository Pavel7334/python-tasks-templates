# Пользователь вводит с клавиатуры курс валют банка в формате $1R60.4
# (1 доллар можно купить по цене в 60.4 рубля) и сумму, которую он
# хочет перевести в другую валюту: 3$ (доллары в рубли) или
# 39578R (рубли в доллары). Выведите полученный результат в терминал.
# Например, 4$ при курсе $1R60.4 -> 241.6R. Обратите внимание,
# что курс валют может быть задан и следующим образом $3R170.05
def app():
    course = float(input())
    summa = float(input())
    print(f'{summa}$ при курсе {course}R за доллар -> {course * summa}R')


if __name__ == "__main__":
    app()
