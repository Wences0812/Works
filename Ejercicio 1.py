def digitos(num, i=0, dig=0):
    if i==len(str(num)):
        return dig
    else:
        return digitos(num, i+1, dig+1)

num=34263469084576
print(digitos(num))