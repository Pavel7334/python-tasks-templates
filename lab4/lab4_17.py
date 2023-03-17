# Дано множество A = {0, 1, 2, 6, 7, 8, 9} и B = {1, 3, 6, 10, 9, 21, 5}. 
# Напишите код для проверки наличия у них общих элементов и 
# выведите полученный результат в терминал.  
# Для решения задачи запрещено использовать циклы.
def app(A: set[int], B: set[int]) -> None:
    common_elements = A.intersection(B)
    print(common_elements)



if __name__ == "__main__":
    A = {0, 1, 2, 6, 7, 8, 9}
    B = {1, 3, 6, 10, 9, 21, 5}
    app(A, B)
