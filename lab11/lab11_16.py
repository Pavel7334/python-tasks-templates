# Напишите функцию fahrenheit_to_celsius, которая осуществляет 
# перевод подаваемого значения (в градусах Фаренгейта) 
# на ее вход в градусы Цельсия и возвращает полученный результат.
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8


if __name__ == "__main__":
    val1 = int(input("Введите температуру "))
    print(fahrenheit_to_celsius(val1))
