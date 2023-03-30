# Напишите функцию max_number, на вход которой подается
# целочисленный список и возвращается его найденное
# максимальное значение.
def max_number(my_list):
    return max(my_list)


if __name__ == "__main__":
    my_list = list(map(int, input().strip().split()))
    print(max_number(my_list))
