import random


filas = 2
columnas = 3
matriz_num_sorteados = []

def rellenar_matriz(matriz_num_sorteados, filas, columnas, lista_sorteados):
    i = 0
    for f in range(filas):
        fila = []
        for c in range(columnas):
            fila.append(lista_sorteados[i])
            i += 1
        matriz_num_sorteados.append(fila)
    return matriz_num_sorteados

def impresion_matriz(matriz_num_sorteados, filas, columnas):
    for f in range(filas):
        for c in range(columnas):
            print("%3d" % matriz_num_sorteados[f][c], end=" ")
        print()



def sorteo_de_nuemros():
    nuemeros_sorteados = []
    while len(nuemeros_sorteados) < 6:
        num_random = random.randint(0, 41)
        if num_random not in nuemeros_sorteados:
            nuemeros_sorteados.append(num_random)

    return nuemeros_sorteados


# Abrir el archivo apuestas.txt
def abrir_archivo():

    archivo = open("apuestas.txt", "rt")
    l = archivo.readline()
    
    ganadores = []
    cont=0
    mayor_numero_coincidente = 0
    while cont <6:
        numero_coincidente = 0

        linea = l.split(";")
        linea[-1] = linea[-1].rstrip('\n')

        for i in range(2, len(linea)):
            num = int(linea[i])
            if num in lista_numeros:
                numero_coincidente += 1

        if numero_coincidente == mayor_numero_coincidente:
            ganadores.append(cont)
        elif numero_coincidente > mayor_numero_coincidente:
            ganadores = []
            ganadores.append(cont)
            mayor_numero_coincidente = numero_coincidente

        cont+=1
        l = archivo.readline()

            

    return ganadores

lista_numeros = sorteo_de_nuemros()
print(lista_numeros)
print(abrir_archivo())

rellenar_matriz(matriz_num_sorteados, filas, columnas, lista_numeros)
impresion_matriz(matriz_num_sorteados, filas, columnas)




        
    





