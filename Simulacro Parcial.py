'''
Desarrollar una función recursiva para duplicar los valores pares de una lista (NO crear una lista nueva).
'''


import os; clear = lambda: os.system('cls'); clear()

def paresLista(lista,i=0):
    if lista!=[]:
        if i == len(lista):   # Ultima posicion de la lista
            return lista
        else:
            num=lista[i]
            if num%2==0:
                num=num*2
                lista[i]=num
            return paresLista(lista,i+1)

lista=[2,6,8,7,3]
print(paresLista(lista))