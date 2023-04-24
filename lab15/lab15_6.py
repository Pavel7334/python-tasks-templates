# Напишите генераторную функцию alphabet, 
# возвращающую по запросу буквы английского 
# алфавита (в строгой последовательности) в нижнем регистре.

def alphabet():
    collection = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,r,q,r,s,t,u,v,w,x,y,z'
    for i in collection.replace(',', ''):
        yield i


if __name__ == "__main__":
    abc = alphabet()
    print(next(abc))
    print(next(abc))
    print(next(abc))
