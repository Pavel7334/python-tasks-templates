# Дана строка str1 = «Цель работы: познакомиться с основными». 
# Проверьте, входит ли в нее символ «м». 
# Полученный результат выведите в терминал.


def app(str1: str) -> None:
    if str1.find('m'):
        print(str1)


if __name__ == '__main__':
    str1 = "Цель работы: познакомиться с основны-ми"
    app(str1)
