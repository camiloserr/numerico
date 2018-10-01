import math

def f(x):
    return x**3 - x*x

def g(x):
    return x/2

def altura(x):
    return math.fabs(f(x) - g(x))

#calcula el area entre las dos curva de a a b con un delta de x = h
def area(a , b , h):
    float(a)
    float(b)
    float(h)
    acum = 0
    i = a
    while i <= b:
        acum  = acum + (altura(i) * h)
        i = i+h

    return acum

print(area( -0.36602540378  , 1.36602540378 , 0.001))

