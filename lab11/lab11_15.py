# Напишите функцию celsius_to_fahrenheit, которая осуществляет 
# перевод подаваемого значения (в градусах Цельсия) на ее 
# вход в градусы Фаренгейта и возвращает полученный результат.
def celsius_to_fahrenheit(celsius):
    return celsius * 34


if __name__ == "__main__":
    val1 = float(input("Введите температуру "))
    print(celsius_to_fahrenheit(val1))
