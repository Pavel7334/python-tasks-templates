# На вход подается 3 значения: start, stop, step.
# Используя списковое включение сформируйте список, 
# элементы которого находятся в диапазоне от start до stop 
# с шагом step и выведите полученный результат в терминал.
def app():
    start = int(input())
    stop = int(input())
    step = int(input())
    print([el for el in range(start, stop, step)])


if __name__ == "__main__":
    app()
