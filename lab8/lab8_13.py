# Пользователь вводит с клавиатуры букву алфавита. Определите является 
# она строчной или прописной и выведите в терминал «lowercase», 
# либо «uppercase» (без кавычек) в зависимости от результата проверки.
def app():
    letter = input()
    if letter.islower():
        print('lowercase')
    if letter.isupper():
        print('uppercase')


if __name__ == "__main__":
    app()
