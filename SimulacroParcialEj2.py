'''
Una empresa que se dedica a fabricar bicicletas, produce de lunes a sábado en n fábricas ubicadas en diferentes lugares del país. Se solicita guardar en una matriz 
la cantidad de bicicletas fabricadas por cada una de sus fábricas durante una semana. Cada columna representa el día de la semana (Lunes columna 0, Martes columna 1,
etc.) y cada fila representa cada una de sus fábricas. El número de fábrica coincide con el número de fila+1 (a continuación se presenta un ejemplo). Se solicita 
crear al menos una función para cada ítem: 

a. Generar al azar (entre 1 y 6) la cantidad de fábricas y simular la cantidad de bicicletas fabricadas para cada día, 
considerando que la capacidad máxima de fabricación es de N unidades y puede suceder que la cantidad sea cero. N se solicita por teclado. Considerando que los 
sábados se trabaja al 50% de la producción, por lo que debe asignar la mitad entera del valor creado al azar. 

b. ¿Cuál es el día menos productivo y a qué día/s 
y fábrica/s pertenece. 

c. Se solicita pasar todas las cantidades fabricadas de la triangular inferior a una lista.

d. Ordenar las cantidades fabricadas de la lista anterior utilizando sort en una determinada rebanada, recibir por parámetro desde y hasta. Por omisión, 
ordenar la lista completa. 
'''
import random
def crearMatriz():
    numBicicletas=int(input("Ingrese la capacidad maxima de bicicletas que se pueden fabricar en un dia: "))
    m=[]
    f=random.randint(1,6)
    for filas in range(f):
        m.append([])
        for columnas in range(7):
            bicicletas=random.randint(1,numBicicletas)
            if columnas==5:
                m[filas].append(bicicletas*0.5)
            else:
                m[filas].append(bicicletas)
    return m
def cantMinimaProducida(m,f=0):
    if m!=[]:
        if f == len(m)-1:   # Ultima fila de la matriz
            minimo = min(m[f])
            return minimo
        else:
            minimo = min(m[f])
            if minimo<cantMinimaProducida(m,f+1):
                posicion= m.index(minimo)
                fabrica=f+1
                return minimo,posicion,fabrica
            return cantMinimaProducida(m,f+1)




m=crearMatriz()
print(m)
print(cantMinimaProducida(m))