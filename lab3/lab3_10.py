# Дан кортеж my_tuple1 = ('a', 'b', 2, 5) и my_tuple2 = (3, 't'). 
# Объедините их в один кортеж my_ tuple3 и 
# выведите в терминал полученный результат.
def app(my_tuple1: tuple, my_tuple2: tuple) -> None:
    my_tuple3 = my_tuple1 +my_tuple2
    print(my_tuple3)


if __name__ == "__main__":
    my_tuple1 = ("a", "b", 2, 5)
    my_tuple2 = (3, "t")
    app(my_tuple1, my_tuple2)
