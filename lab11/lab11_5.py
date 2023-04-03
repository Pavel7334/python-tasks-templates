#Напишите функцию find_list_index, на вход которой подается список и искомое 
# в нем значение и возвращающую номер индекса, по которому это значение хранится. 
# Если элемента с искомым значением нет в списке – верните None. 
def find_list_index(my_list, value):
    return my_list.index(value)




if __name__ == "__main__":
    my_list = list(map(int, input().strip().split()))
    my_var1 = int(input("Введите искомое значение "))

    print(find_list_index(my_list, my_var1))
