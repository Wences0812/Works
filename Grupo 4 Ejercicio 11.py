"""
Desarrollar una funcion que devuelva el minimo elemento de una matriz de N x M
"""
def minimoMatriz(m,f=0):
    if m!=[]:
        if f == len(m)-1:   # Ultima fila de la matriz (3)
            minimo = min(m[f])
            return minimo
        else:
            minimo = min(m[f])
            if minimo<minimoMatriz(m,f+1):
                return minimo
            return minimoMatriz(m,f+1)


def maximoMatriz(m,f=0):
    if m!=[]:
        if f == len(m)-1:   # Ultima fila de la matriz (3)
            maximo = max(m[f])
            return maximo
        else:
            maximo = max(m[f])
            if maximo>maximoMatriz(m,f+1):
                return maximo
            return maximoMatriz(m,f+1)


#Programa Principal
# m= [[8,7,4],[8,5,6],[5,8,9],[10,11,12]] 
m= [[8,7,4],[11,8,5,-6],[5,2,9]] 
print(minimoMatriz(m))
print(maximoMatriz(m))
