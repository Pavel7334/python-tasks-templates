# Напишите декоратор celsius, который будет переводить в градусы 
# Цельсия возвращаемое значение функцией temperature_fahrenheit, 
# на вход которой подается значение температуры в градусах Фаренгейта, 
# и оно же возвращается. 


def celsius(func):
    def helper(tem):
        celsius = int(func((5 / 9) * (tem - 32)))
        return celsius
    return helper


@celsius
def temperature_fahrenheit(tem: int) -> int:
    return tem


if __name__ == "__main__":
    print(temperature_fahrenheit(32)) # 0
