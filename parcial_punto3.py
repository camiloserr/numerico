def relax(a,b,x,w):

    r = int(input("numero de iteraciones: "))
    for it in range(r):
        nn = len(x)
        for i in range(nn):
            s=0
            for j in range(nn):
                if i!=j:
                    s = s+a[i][j]*x[j]
            anterior = x[i];
            x[i] = (b[i]-s)/a[i][i]
            #aca se aplica el factor de relajación
            x[i] = w*x[i] + (1-w)*anterior;

    return x




# 3x-y-z=-1
# -x+3y+1=3
# 2x+y+4z=7


w = 0.8
a = [[4,-1,-1,-1] , [-1,4,-1,-1], [-1,-1,4,-1] , [-1,-1,-1,4]]

b=[]

print ("Ingrese el vector solucion de la matriz")
b.clear()
for i in range(len(a)):
    mensaje = "B(" + str(i) + ") = "
    k = int(input(mensaje) )
    b.append(k)

#valores iniciales

x=[]

for i in range(len(a)):
    x.append(0);



y = relax(a,b,x,w);

for i in range(len(y)):
    print("x",i+1, " = " , y[i]);
