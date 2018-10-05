import math

def f(x):
    return -4 * x ** 3 + 60 * x * x - 4 * x + 2

#retorna la distancia euclidiana entre dos puntos
def dist(x1 , y1 , x2 , y2):
    return math.sqrt( math.fabs(x2 - x1)**2 + math.fabs(y2 - y1)**2 )



#calcula la suma de la longitud da las rectas secantes
def longitud(a , b , part):
    i = a
    h = (math.fabs(a-b))/part
    res = 0
    ant = f(i)
    #le suma la longitud de la recta secante entre f(i) y f(i+h)
    while i < b:

        nueva = f(i+h)
        res = res + dist(i , ant , i+h , nueva)
        ant = nueva
        i = i+h

    return res

a = float(input("x inicial: "))
b = float(input("x final: "))
part = float(input("numero de particiones: "))

print(longitud(a , b , part))

