# Напишите генераторную функцию letters, на вход которой 
# подается строка и она посимвольно возвращает поданное 
# на вход значение при инициализации генератора.

def letters(my_str: str) -> str:
    for i in my_str:
        yield i

if __name__ == "__main__":
    my_str = "qwerty"

    for i in letters(my_str):
        print(i)
