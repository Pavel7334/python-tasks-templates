# Дана строковая переменная, которой присваивается любое слово. 
# Напишите программу, которая формирует новую переменную путем 
# удаления символов из первой строки (с нулевого элемента по 3-й). 
# Полученный результат выведите в терминал. 
# Например: «МамаМылаРаму» -> «МылаРаму».

def app(str1: str) -> None:
    print(str1[4:])
    # print(''.join([str1[i] for i in range(len(str1)) if i > 3]))  ###второй вариант

if __name__ == '__main__':
    str1 = "МамаМылаРаму"
    app(str1)
