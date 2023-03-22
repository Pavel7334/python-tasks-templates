# На вход подается список my_list.
# Если его первый и последний элементы равны, 
# то выведите в терминал «True», иначе «False» (без кавычек).
def app():
    my_list = list(map(int, input().strip().split()))
    print(my_list[0] == my_list[-1])


if __name__ == "__main__":
    app()
