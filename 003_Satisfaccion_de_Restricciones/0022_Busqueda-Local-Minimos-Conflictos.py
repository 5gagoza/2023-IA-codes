"""
el código implementa el algoritmo de búsqueda local Mínimos-Conflictos para resolver un problema de asignación de colores a un grafo. 
El objetivo es encontrar una asignación de colores que minimice la cantidad de conflictos entre nodos adyacentes, es decir, nodos que comparten una arista.
"""

import random

# Función que genera un estado inicial aleatorio
def generar_estado_inicial(n):
    return [random.randint(1, n) for i in range(n)]

# Función que calcula el número de conflictos en un estado
def calcular_conflictos(estado):
    n = len(estado)
    num_conflictos = 0
    for i in range(n):
        for j in range(i+1, n):
            if estado[i] == estado[j] or abs(i-j) == abs(estado[i]-estado[j]):
                num_conflictos += 1
    return num_conflictos

# Función que devuelve una lista de los valores que minimizan el número de conflictos
def minimizar_conflictos(estado):
    n = len(estado)
    mejores_valores = []
    min_conflictos = n**2  # Inicialmente se establece un valor máximo de conflictos
    for i in range(n):
        for j in range(1, n+1):
            if estado[i] != j:
                nuevo_estado = estado.copy()
                nuevo_estado[i] = j
                num_conflictos = calcular_conflictos(nuevo_estado)
                if num_conflictos < min_conflictos:
                    mejores_valores = [j]
                    min_conflictos = num_conflictos
                elif num_conflictos == min_conflictos:
                    mejores_valores.append(j)
    return mejores_valores

# Función que implementa el algoritmo de mínimos conflictos
def minimos_conflictos(n, max_iteraciones):
    estado_actual = generar_estado_inicial(n)
    for i in range(max_iteraciones):
        num_conflictos = calcular_conflictos(estado_actual)
        if num_conflictos == 0:
            return estado_actual
        columna = random.randint(0, n-1)
        mejores_valores = minimizar_conflictos(estado_actual)
        nuevo_valor = random.choice(mejores_valores)
        estado_actual[columna] = nuevo_valor
    return None

# Ejemplo de uso
n = 8
max_iteraciones = 1000
solucion = minimos_conflictos(n, max_iteraciones)
if solucion is not None:
    print("Se encontró una solución:")
    print(solucion)
else:
    print("No se encontró una solución en el número máximo de iteraciones.")

