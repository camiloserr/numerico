def seidel(a,b,x):

    r = int(input("numero de iteraciones: "))
    for it in range(r):
        nn = len(x)
        for i in range(nn):
            s=0
            for j in range(nn):
                if i!=j:
                    s = s+a[i][j]*x[j]
            x[i] = (b[i]-s)/a[i][i]

    return x


# 3x-y-z=-1
# -x+3y+1=3
# 2x+y+4z=7

#a = [[3, -1, -1], [-1, 3, 1], [2, 1, 4]]
#b = [1, 3, 7]

#valores iniciales
#x = [0, 0, 0]

a = []
b = []

#valores iniciales
x = []

n = int(input("ingrese el numero de filas de la matriz A: ") )
m = int(input("ingrese el numero de columnas de la matriz A: ") )

mensaje = ""

print("Ingrese la matriz A")
for i in range(n):
    aux = []
    for j in range(m):
        mensaje = "A(" + str(i) + " , " + str(j) + ") = "
        k = int(input(mensaje) )
        aux.append(k)

    a.append(aux)


for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j] ," ", end=" ")
    print(" ")



print ("Ingrese el vector solucion de la matriz")
b.clear()
for i in range(n):
    mensaje = "B(" + str(i) + ") = "
    k = int(input(mensaje) )
    b.append(k)


print ("Ingrese los valores iniciales de Xn")

for i in range(n):
    mensaje = "X(" + str(i) + ") = "
    k = int(input(mensaje) )
    x.append(k)

flag = True
if(m > n):
    print("Infinitas soluciones.")
elif(n == m):
    y = seidel(a,b,x)
else:
    y = seidel(temp,b)
    for i in range(len(x)+1,n):
        result = 0
        for j in range(m):
            result += a[i][j]*y[j]

        if(result != b[i]):
            flag = False
if(flag):
    for i in  range (len(y)):
        print("x",i," = " ,y[i])
else:
    print("No tiene solucion.")
