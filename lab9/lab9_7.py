# На вход подается список my_list. Используя цикл while 
# посчитайте количество вхождения в него элементов со 
# значением 2 и выведите в терминал полученный результат.
def app():
    my_list = list(map(int, input().strip().split()))
    i = 0
    count = 0
    while i < len(my_list):
        if my_list[i] == 2:
            count += 1
        i += 1
    print(count)


if __name__ == "__main__":
    app()
