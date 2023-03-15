# Дан список my_list = [1, 2, 3, 4, 5, 6]. 
# Выведите в терминал его размер.

def app(my_list: list[int]) -> None:
    print(len(my_list))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6]
    app(my_list)
