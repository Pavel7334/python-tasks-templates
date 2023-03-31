#Напишите функцию multiply, возвращающую произведение 
# элементов из поступающего на ее вход списка.
def multiply(my_list):
    return my_list * my_list




if __name__ == "__main__":
    my_list = list(map(int, input().strip().split()))
    print(multiply(my_list))
