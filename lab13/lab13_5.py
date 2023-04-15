# На вход функции closure_comparison поступает один из символов «>», 
# «<», «=». Используя механизм замыканий, сравните два значения a и b, 
# подаваемые на вход возвращаемой функции. В результате должно 
# возвращаться True, если результат сравнения ИСТИНА, иначе – False. 
# В том случае, когда на вход closure_ comparison подается 
# неизвестный символ – результат всегда False.

def closure_comparison(symbol: str) -> bool:
    def helper(a, b):
        if symbol == "=":
            return a == b
        if symbol == ">":
            return a > b
        if symbol == "<":
            return a < b
        if symbol == "!=":
            return False
    return helper

if __name__ == "__main__":
    x = closure_comparison("=")
    print(x(2, 2))
    print(x(2, 3))
    x = closure_comparison(">")
    print(x(2, 2))
    print(x(3, 2))
    x = closure_comparison("<")
    print(x(2, 2))
    print(x(2, 3))
    print(closure_comparison("!=")(2, 3))