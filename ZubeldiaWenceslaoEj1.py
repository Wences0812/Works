'''
Escribir una función recursiva en Python que dada una cadena determine si en la misma hay más letras I o letras U.
Resolver sin utilizar rebanadas y sin crear estructuras auxiliares. Explique la estrategia con la que piensa resolver 
este problema.

'''
import os; clear = lambda: os.system('cls'); clear()


def letrasLista(cadena, canti=0, cantU=0, i=0):
    if i==len(cadena):  #Cuando llega al ultimo elemento hace un return de las i e u que hay en la cadena
        return canti, cantU
    else:
        letra=cadena[i].lower()
        if letra=='i':  #Si la letra en la posicion i es 'i' incremento mi variable de canti que son las cantidades de i en la cadena.
            canti += 1
        if letra=='u':  #Si la letra en la posicion i es 'u' incremento mi variable de cantU que son las cantidades de u en la cadena.
            cantU += 1
        return(letrasLista(cadena, canti, cantU, i+1))

cadena="uuiii"
if cadena=="":
    print("No ingreso ninguna cadena.")
else:
    cadenaF=letrasLista(cadena)
    if cadenaF[0]==0 and cadenaF[1]==0:
        print("No hay i ni u en la lista")
    else:
        if cadenaF[0]>cadenaF[1]:
            print("Hay mas letras i que letras u")
        elif cadenaF[0]==cadenaF[1]:
            print("Tienen la misma cantidad de u que de i")
        else:
            print("Hay mas letras u que letras i")
