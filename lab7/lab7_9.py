# На вход подается список my_list (значения через пробел). 
# Найдите произведение его второго и среднего элемента 
# и выведите полученный результат в терминал.
def app():
    my_list = list(map(int, input().strip().split()))
    print(my_list[1] * my_list[len(my_list) // 2])


if __name__ == "__main__":
    app()
