import numpy

E = 10**(-7)

def g1(x):
    return numpy.log(x+2);

def g2(x):
    return numpy.sin(x);
    

#ya que el algoritmo me permite hallar raices    
#la funcion f(x) = ln(x+2) - sin(x)
#y lo utilizo para hallar f(x) = 0 , es decir ln(x+2) = sin(X)


def f(x):
    return g1(x) - g2(x);
    


def func(x1 , x2):
    
    if  f(x1) - f(x2) == 0:
        return "error en el intervalo";
    
    nuevo = x1 - ((f(x1) * (x1 - x2))/( f(x1) - f(x2)));
    print(nuevo);
    if numpy.fabs(nuevo - x1) < E:
        return nuevo;
    return func(nuevo , x1);
    
    

#se escogieron los valores iniciales por media de la grafica de las dos funciones

try:
    print(func(-2 , -1));
except RuntimeError as re:
    print ("el algoritmo no converge con esos valores ")

#este metodo con esta funcion es extremadamente sensible a los valores iniciales


