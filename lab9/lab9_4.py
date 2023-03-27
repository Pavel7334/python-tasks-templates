# На вход подается список my_list. Используя цикл for 
# найдите сумму элементов с нечетным индексом и 
# выведите полученный результат в терминал.
def app():
    my_list = list(map(int, input().strip().split()))
    count = 0
    for i in range(1, len(my_list), 2):
        count += my_list[i]
    print(count)


if __name__ == "__main__":
    app()
