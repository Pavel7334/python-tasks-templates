# Напишите программу переворачивающую строку «Как дела?» без использования циклов. 
# Полученный результат выведите в терминал. 
# Например: «Йо-хо-хо!» -> «!ох-ох-оЙ».


def app(str1: str) -> None:
    print(str1[::-1])

    print("".join(reversed(str1)))

    chars = list(str1)
    for i in range(len(str1) // 2):
        tmp = chars[i]
        chars[i] = chars[len(str1) - i - 1]
        chars[len(str1) - i - 1] = tmp
    print(''.join(chars))


if __name__ == '__main__':
    str1 = "Как дела?"
    app(str1)
