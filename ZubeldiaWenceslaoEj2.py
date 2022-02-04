'''
Hacer un programa en Python que solicite al usuario el tamaño de una matriz cuadrada. Luego genere una matriz con 
valores ingresados por teclado y verifique si la matriz es simétrica con respecto a la su diagonal secundaria. 
Al finalizar mostrar la matriz. Explique la estrategia con la que piensa resolver este problema. 

'''
import os; clear = lambda: os.system('cls'); clear()

def crearMatriz(f,c):
    '''
    pre: se ingresan la cantidad de filas y columnas que el cliente desee tener la matriz.
    pos: se devuelve una matriz llena con los numeros cargados por teclado.
    '''
    m=[]
    for filas in range (f):
        m.append([])
        for columnas in range(c):
            num=int(input("Ingrese numeros para llenar la matriz: "))
            while num=='':
                print("No ha ingresado nada.")
                num=int(input("Ingrese numeros para llenar la matriz: "))
            m[filas].append(num)
    return m

def simetrica(m,f=0,c=0,cont=0):
    '''
    pre: Recibo una matriz cuadrada.
    pos: Devuelvo si es simetrica o no.
    '''
    if len(m)==f and c==0: #Final de la diagonal secundaria
        return cont
    else:
        c=len(m[0])
        c=c-cont-1  #Voy restando el contador a la columna en la que estoy para asi ir calculando solo la diagonal secundaria, no cualquier elemento.
        cont += 1
        return(simetrica(m,f+1,c,cont))

def MostrarMatriz(m):
    '''
    pre: Se recibe la matriz a mostrar.
    pos: Se muestran por consola, los elementos de la matriz de una forma mas prolija.
    '''
    filas=len(m)
    columnas=len(m[0])
    for f in range(filas):
        for c in range (columnas):
            print(f'{m[f][c]:8d}',end="")
        print() #Salto de linea entre fila y fila.
    return m

f=int(input("Ingrese el numero de filas de la matriz:"))
c=int(input("Ingrese el numero de columnas de la matriz:"))
while f!=c: #Verifico si es simetrica(cuadrada).
    print("Ingrese una matriz cuadrada!")
    f=int(input("Ingrese el numero de filas de la matriz:"))
    c=int(input("Ingrese el numero de columnas de la matriz:"))
m=crearMatriz(f,c)
MostrarMatriz(m)
gradoMatriz=simetrica(m)
print("La matriz es simetrica y es de grado",gradoMatriz)