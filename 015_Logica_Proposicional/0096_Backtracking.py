


"""Bactracking:

    Es una búsqueda exhaustiva de todas las posibles soluciones.
    En caso de llegar a una solución inválida se retrocede.

    Primero se identifican las restricciones y el espacio de búsqueda.
    Se define una estructura de datos.
    Se crea una función recursiva para buscar las soluciones.
    La función creará soluciones parciales y las evaluará para ver que se cumplan.
    Dando como resultado las soluciones validas al problema.    

"""
# Definimos los elementos que queremos combinar, una combinación en construcción y todas las combinaciones validas

def backtrack(lista, combinacion_actual, todas_combinaciones):
    # Condición de terminación: Si la combinación actual es válida, la agregamos a la lista de todas las combinaciones
    if len(combinacion_actual) == len(lista):
        todas_combinaciones.append(combinacion_actual[:])
        return
    
    # Generar todas las posibles elecciones
    for elemento in lista:
        if elemento not in combinacion_actual:      # Checamos si el elemento está en la lista
            # Hacer una elección
            combinacion_actual.append(elemento)     # Lo agragamos a la combinación si no está
            
            # Llamar recursivamente al backtrack con la elección actual
            backtrack(lista, combinacion_actual, todas_combinaciones)       # Checamos otras combinaciones en base a la elección actual.
            
            # Deshacer la elección para el backtrack
            combinacion_actual.pop()        #Para poder elegir otras elecciones

# Ejemplo de uso
elementos = [1, 2, 3]
combinaciones = []
backtrack(elementos, [], combinaciones)

# Imprimir todas las combinaciones
for combinacion in combinaciones:
    print(combinacion)
