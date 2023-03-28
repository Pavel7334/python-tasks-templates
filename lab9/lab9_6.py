# На вход подается список my_list. Используя цикл while найдите
# сумму элементов с нечетным индексом и выведите полученный 
# результат в терминал.
def app():
    my_list = list(map(int, input().strip().split()))
    i = 1
    amount = 0

    # цикл вычисления суммы
    while i < len(my_list):
        amount += my_list[i]
        i += 1
    print("Сумма =", amount)


if __name__ == "__main__":
    app()
