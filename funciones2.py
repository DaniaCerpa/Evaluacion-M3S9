#Creación de funciones:

def suma (a,b):
    return (a + b)

def resta (a,b):
    return (a - b)

def multiplicacion (a,b):
    return (a * b)

def division (a,b):
    return (a / b)


#Creación de funcion contenedora

def variables_tuplas (a,b):
    tuplas_num = (suma(a,b), resta(a,b), multiplicacion(a,b), division(a,b)) 
    diccionario = {"Suma": tuplas_num[0], "Resta": tuplas_num[1], "Multiplicación": tuplas_num[2], "division": tuplas_num[3]}
    return diccionario


#Ejemplo para ejecución

print (variables_tuplas(15,20))

