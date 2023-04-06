# Напишите функцию max_count, на вход которой подается 
# целочисленный список и возвращается значение элемента, 
# который встречается наибольшее число раз.
def max_count(lst: list) -> int:
    new_dict = {}

    for i in lst:
        if i not in new_dict:
            new_dict[i] = lst.count(i)
    sorted_keys = sorted(new_dict, key=new_dict.get)

    return sorted_keys[-1]


if __name__ == "__main__":
    my_list = list(map(int, input().strip().split()))
    print(max_count(my_list))
