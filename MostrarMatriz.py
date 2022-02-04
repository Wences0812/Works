def CrearMatriz(f,c):
    #pre: Se ingresan el numero de filas (f) y columnas (c) deseados.
    #pos: Se devuelve una matriz de fxc creada con ceros.
    
    matriz=[]
    for filas in range (f):
        matriz.append([])
        for columnas in range(c):
            matriz[filas].append(0)
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
    return m

f=int(input("Ingrese el numero de filas de la matriz:"))
c=int(input("Ingrese el numero de columnas de la matriz:"))

m=CrearMatriz(f,c)
mFinal=MostrarMatriz(m)