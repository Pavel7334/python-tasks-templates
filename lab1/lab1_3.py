# Дана строка str1 = «Цель работы: познакомиться с основными». 
# Посчитайте количество вхождений в нее символа «о» и 
# выведите полученный результат в терминал. 
# Циклы использовать запрещено.


def app(str1: str) -> None:
    print(str1.count("о"))


if __name__ == '__main__':
    str1 = "Цель работы: познакомиться с основны-ми"
    app(str1)