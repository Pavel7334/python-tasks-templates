# Напишите функцию is_generator, принимающую на вход другую функцию 
# и возвращающую True, если передается генераторная функция, иначе – False.
import types


# def is_generator(func):
#     if func != types.GeneratorType:
#         return False


if __name__ == "__main__":
    def my_gen():
        yield 1


    print(is_generator(my_gen))
    print(is_generator(10))
