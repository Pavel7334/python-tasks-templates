# На вход подается список my_list. Используя цикл for посчитайте 
# сумму значений, которые нацело делятся на 3 и выведите в 
# терминал полученный результат.
def app():
    summa = 0
    my_list = list(map(int, input().strip().split()))
    for i in my_list:
        if i % 3 == 0:
            summa += i
    print(summa)


if __name__ == "__main__":
    app()
