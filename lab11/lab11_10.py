# Напишите функцию pow3, возводящую в куб подаваемое 
# на вход значение и возвращающую полученный результат.
def pow3(my_var1):
    return my_var1 ** 3


if __name__ == "__main__":
    my_var1 = int(input("Введите значение "))

    print(pow3(my_var1))
