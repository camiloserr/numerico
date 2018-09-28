import math

def f(x):
	return (1/(math.sqrt(2 * math.pi))) * (math.e ** -(x*x /2 ))

h = 10**-4
inf = 5
x= -inf
acum = 0

while x < 1:
    acum = acum + (h*(f(x) + f (x+h) ) /2 )
    x+=h
print(x,"=",acum)

