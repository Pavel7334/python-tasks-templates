# На вход подается список my_list. Используя цикл while 
# найдите сумму его элементов и выведите полученный 
# результат в терминал.
def app():
    my_list = list(map(int, input().strip().split()))
    i = 0
    amount = 0

    # цикл вычисления суммы
    while i < len(my_list):
        amount = amount + my_list[i]
        i += 1
    print("Сумма =", amount)


if __name__ == "__main__":
    app()
