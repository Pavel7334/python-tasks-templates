# На вход подается список my_list. Если значение в середине списка больше, 
# либо равно 10, то выведите в терминал сумму его первого и последнего 
# элемента, иначе произведение первого и предпоследнего.
def app():
    my_list = list(map(int, input().strip().split()))
    if my_list[len(my_list) // 2] >= 10:
        print(my_list[0] + my_list[-1])
    if my_list[len(my_list) // 2] < 10:
        print(my_list[0] * my_list[-2])






if __name__ == "__main__":
    app()
