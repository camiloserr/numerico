from sympy import*
import numpy as np
import math
import matplotlib.pyplot as plot

def crearX(a,b,n):
    x = []
    for i in range(n):
        x.append(math.cos(((2*i +1)/(2*n +2))*math.pi))
        print(math.cos(((2*i +1)/(2*n +2))*math.pi))
    return x

def f(x):
    return math.e ** x
def crearY(x):
    y = []
    for i in range(len( x )):
        y.append(f(x[i]))
    return y

def lagrange(x,y,u=None):
    n = len(x)
    t = Symbol('t')
    p = 0
    for i in range(n):
        L=1
        for j in range(n):
            if j!=i:
                L=L*(t-x[j])/(x[i]-x[j])
        p = p+y[i]*L
        p = expand(p)
    if u==None:
        return p
    else:
        r=p.subs(t,u)
        return r

#x=[0.3,0.4,0.5,0.6]
#y=[0.33,0.34,0.45,0.46]
x = crearX(-1,1,10)
y = crearY(x)
p = lagrange(x,y)
print(p)
r = lagrange(x,y,0)
print(r)
plot.plot(x,y)
plot.show()
