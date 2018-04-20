import math

def fun(n):
    for b in range(n):
        for a in range(1, b):
            c = math.sqrt( a * a + b * b)
            if c % 1 == 0:
                print (a, b, int(c))

num = int(input("Enter Number"))
fun(num)
