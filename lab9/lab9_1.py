# На вход подается список my_list. Используя цикл for 
# найдите сумму его элементов и выведите полученный результат в терминал.
def app():
    my_list = list(map(int, input().strip().split()))
    count = 0
    for i in my_list:
        count += i
    print(count)


if __name__ == "__main__":
    app()
