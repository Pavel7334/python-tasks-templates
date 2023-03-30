# Пользователь вводит с клавиатуры размерность матрицы – N. 
# Используя механизм списковых включений сформируйте единичную матрицу N×N 
# и выведите полученный результат в терминал.
def app():
    size = int(input())
    matrix = list([[1 if i == j else 0 for j in range(size)] for i in range(size)])
    print(*matrix, sep='\n')


if __name__ == "__main__":
    app()
