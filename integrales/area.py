import math
import numpy as np
import matplotlib.pyplot as plt

inf = 99999999

def f(x):
    return math.cos(x)

def g(x):
    return math.sin(x)

def altura(x):
    return math.fabs(f(x) - g(x))

def error( cota , h):
    return cota * h*h

#calcula el area entre las dos curva de a a b con un delta de x = h
def area(a , b , h):
    float(a)
    float(b)
    float(h)
    acum = 0
    i = a
    while i <= b:
        acum  = acum + ( ((altura(i) + altura(i+h) )/2) * h)
        i = i+h
    return acum

    
#calcula el area entre la curva
def area2(a , b , h):
    float(a)
    float(b)
    float(h)
    acum = 0
    i = a
    mayor = -inf
    while i <= b:
        absf = math.fabs(f(i))
        absg = math.fabs(g(i))
        mayor = max(mayor , absf)
        mayor = max(mayor , absg)
        if absf > absg:
            acum  = acum + ( ((absg  )) * h)
        else:
            acum  = acum + ( ((absf  )) * h)
        i = i+h
    print("error =",error(mayor,h))
    return acum


def plotear(ini , fin ):
    x = np.arange(ini,fin, 0.01)
    y1 = []
    y2 = []
    for i in range(len(x)):
        y1.append(f(x[i]))
        y2.append(g(x[i]))

    fig, ax = plt.subplots()
    ax.plot(x, y1, x, y2, color='black')
    ax.fill_between(x, y1, y2, where=y2 >= y1, facecolor='green', interpolate=True)
    ax.fill_between(x, y1, y2, where=y2 <= y1, facecolor='green', interpolate=True)
    ax.set_title('area entre las dos funciones')
    plt.show()


def main():
    ini = float(input("Valor inicial x: "))
    fin = float(input("Valor final x: "))
    part = float(input("numero de particiones: "))
    print("h =",(fin-ini)/part)
    print(area2(ini, fin, (fin-ini)/part))
    plotear(ini , fin)


main()
