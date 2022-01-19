def f(x):
    return 10 - (3 * x * x )
x0 = float (input("Enter value of x0 "))
xn = float (input("Enter value of xn "))
n = int (input("Enter intervals "))
def sim(x0,xn,n):
    h = (xn -x0)/n
    int = f(x0) + f(xn)
    for i in range(1,n):
        k = x0 + i*h
        if i%2 ==0:
            int = int + 2* f(k)
        else:
            int = int + 4* f(k)
    int = int * (h/3)
    return int
ans = sim(-1,3,4)
print (" Integration is: ",ans) 

