# Напишите функцию closure_sum, использующую механизм замыканий 
# для сложения двух чисел и возвращающую полученное значение. 
# Например, closure_sum(1)(2) -> 3.

def closure_sum(a):
    def helper(b):
        return a + b

    return helper

if __name__ == "__main__":
    print(closure_sum(1)(2))
    x = closure_sum(10)
    print(x(2))
    print(x(-2))
