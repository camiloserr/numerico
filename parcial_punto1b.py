def sumar(a):
    cont = 0;
    operaciones = 0
    for i in range(len(a)):
        
        for j in range (len ( a[i] )):
            cont  = cont + a[i][j];
            operaciones = operaciones+1;
            
    print("con n = ",len(a),":");
    print("numero de operaciones: " , operaciones);
    print("respuesta: ",cont);
    return cont;
    
    
a = [ [1,2] , [3,4]]

b = [ [-8,4] , [10,-5] ]

c = [ [-8,4 , 7 ,12] , [10 , -1 , 9,-5], [1 , 66 , -40 , 12] , [2 , -1 , 0,3] ]

#con n = 2
sumar(a)
print();
#con n = 2
sumar(b)
print();
#con n = 4
sumar(c)
print();


#La complejidad de este algoritmo es de O(n^2)
#ya que en una matriz de nxn se debe hace una operacion de suma para cada elemento
