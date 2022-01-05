import numpy as np
def f(x):
    return x * x - 10
def g(x):
    return 2 * x
x = float(input("enter starting number"))
n = int (input("Number of interations"))
e=1
while (e<=n):
    y=x-f(x)/g(x)
    e=e+1
    x=y
print("the root of the equation is",x)
