def digitos(num, i=0, dig=0):
    if i==len(str(num)):
        return dig
    else:
        return digitos(num, i+1, dig+1)

def binario(digitosNum, num):
    suma=0
    listNum=[]
    for i in range(len(str(num))):
        listNum.append(str(num)[i])
    listNum.reverse()
    for i in range(len(str(num))):
        if listNum[i]=='1':
            suma+=2**i
    return suma

num= int(input("Ingrese su numero para pasarlo a binario: "))
digitosNum=digitos(num)
print("El numero tiene",digitosNum,"dígitos.")
numPasado=binario(digitosNum, num)
print("Su numero es:",numPasado)