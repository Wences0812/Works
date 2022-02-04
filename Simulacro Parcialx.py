'''
Desarrollar un programa que utilice una funcion que reciba por parametro una matriz de enteros 
de NxN y devuelva el valor que mas se repite en la misma, o todos los que corresponden en el caso 
de haber mas de uno. La matriz se debe cargar con numeros al azar entre 0 y 9. El valor de N se 
ingresa desde el teclado.
'''
import random

def CrearMatriz(n):
    #pre: Se ingresan el numero de filas (f) y columnas (c) deseados.
    #pos: Se devuelve una matriz de fxc creada con ceros.
    
    matriz=[]
    for filas in range (n):
        matriz.append([])
        for columnas in range(n):
            num=random.randint(0,9)
            matriz[filas].append(num)
    return matriz

def MostrarMatriz(m):
    #pre: Se recibe la matriz a mostrar.
    #pos: Se muestran por consola, los elementos de la matriz.
    filas=len(m)
    columnas=len(m[0])
    for f in range(filas):
        for c in range (columnas):
            print(f'{m[f][c]:8d}',end="")
        print() #Salto de linea entre fila y fila.

n=int(input("Ingrese la cantidad de filas y columnas que quiera que tenga su matriz: "))
m=CrearMatriz(n)
print(MostrarMatriz(m))