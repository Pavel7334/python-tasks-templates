# На вход подается список my_list. Используя цикл for посчитайте 
# количество вхождения в него элементов со значением 2 и выведите 
# в терминал полученный результат. 
def app():
    my_list = list(map(int, input().strip().split()))
    count = 0
    for i in my_list:
        if i == 2:
            count += 1
    print(count)


if __name__ == "__main__":
    app()
