# Напишите декоратор fahrenheit, который будет переводить в градусы Фаренгейта 
# возвращаемое значение функцией temperature_celsius, 
# на вход которой подается значение температуры в градусах Цельсия, 
# и оно же возвращается. 


def fahrenheit(func):
    def helper(tem):
        return int(func(((tem * 9) / 5) + 32))
    return helper


@fahrenheit
def temperature_celsius(tem: int) -> int:
    return tem


if __name__ == "__main__":
    my_temp1 = 0
    print(temperature_celsius(my_temp1)) # 32
