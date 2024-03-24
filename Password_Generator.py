def pass1():
    import numpy
    from numpy import random as rd
    k=int(input("ENTER THE LENGTH OF PASSWORD: "))
    l="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    p=""
    for i in range(1,k+1):
        r=rd.randint(52)
        p=p+l[r]
    print(p)
r=int(input("HOW MANY PASSWORD YOU WANT TO GENERATE: "))
for j in range(r):
    pass1()
