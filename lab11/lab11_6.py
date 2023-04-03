#Напишите функцию find_dict_key, на вход которой подается 
# словарь и искомое в нем значение и возвращающую ключ по 
# которому оно хранится. Если элемента с искомым 
# значением нет – верните None.
def find_dict_key(my_dict, value):
    for k, new_va in my_dict.items():
        if value == new_va:
            return k
        else:
            return None


if __name__ == "__main__":
    my_dict1 = {1: "a", 2: "b", 3: "c"}
    my_var1 = input("Введите искомое значение ")

    print(find_dict_key(my_dict1, my_var1))
