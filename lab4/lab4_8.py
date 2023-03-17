# Дан список my_list = [1, 0, 'Hi', 10] и множество my_set = {3, 5, 'b'}. 
# Добавьте элементы списка в множество не используя циклы и 
# выведите в терминал полученный результат.
def app(my_list: list, my_set: set) -> None:
    print(my_set.union(set(my_list)))


if __name__ == "__main__":
    my_list = [1, 0, "Hi", 10]
    my_set = {3, 5, "b"}
    app(my_list, my_set)
