import numpy as np
a = -2
b = 2
n = 100
h = (b - a) / (n - 1)
x = np.linspace(a,b,n)
f = 10 - x*x
Itrap = h* ((f[a] + f[b])/2 + sum(f[1:n-1]))
Iptrap = float (Itrap)
print(float(Itrap))

