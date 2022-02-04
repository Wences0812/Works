'''
Listado de pacientes mayores a una determinada edad ingresada por teclado
'''
listaMayores=[]
def lista_mayores(paciente,edadPaciente,edad,listaMayores):
    if edadPaciente>edad:
        listaMayores.append(paciente)
    return listaMayores

paciente='Juan'
edadPaciente=79
edad=int(input("Ingrese la edad en minima de los clientes mayores: "))
print(lista_mayores(paciente,edadPaciente,edad,listaMayores))