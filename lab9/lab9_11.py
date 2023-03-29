# На вход подается список my_list. Используя цикл while  посчитайте 
# сумму значений, которые нацело делятся на 4 и выведите в 
# терминал полученный результат.
def app():
    my_list = list(map(int, input().strip().split()))
    i = 0
    summa = 0
    while i < len(my_list):
        if my_list[i] % 4 == 0:
            summa += my_list[i]
        i += 1
    print(summa)


if __name__ == "__main__":
    app()
