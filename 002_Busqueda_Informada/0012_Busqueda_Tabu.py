import random

def busqueda_tabu(solucion_inicial, funcion_objetivo, vecindario, longitud_tabu, max_iter):
    """
    Busca la mejor solución aplicando el algoritmo de búsqueda tabú.
    
    :param solucion_inicial: La solución inicial desde la cual comenzar la búsqueda.
    :param funcion_objetivo: La función objetivo que se quiere optimizar.
    :param vecindario: La función que devuelve el vecindario de una solución.
    :param longitud_tabu: La longitud de la lista tabú.
    :param max_iter: El número máximo de iteraciones permitidas.
    :return: La mejor solución encontrada.
    """
    mejor_solucion = solucion_inicial
    mejor_valor = funcion_objetivo(mejor_solucion)
    lista_tabu = []
    
    for i in range(max_iter):
        vecinos = vecindario(mejor_solucion)
        vecinos_filtrados = [vecino for vecino in vecinos if vecino not in lista_tabu]
        
        if vecinos_filtrados:
            nueva_solucion = max(vecinos_filtrados, key=funcion_objetivo)
            nuevo_valor = funcion_objetivo(nueva_solucion)
            
            if nuevo_valor > mejor_valor:
                mejor_solucion = nueva_solucion
                mejor_valor = nuevo_valor
                
            lista_tabu.append(mejor_solucion)
            
            if len(lista_tabu) > longitud_tabu:
                lista_tabu.pop(0)
        
        else:
            # Si no hay vecinos no visitados, se elige uno aleatoriamente
            nueva_solucion = random.choice(vecinos)
            nuevo_valor = funcion_objetivo(nueva_solucion)
            lista_tabu.append(nueva_solucion)
            
            if len(lista_tabu) > longitud_tabu:
                lista_tabu.pop(0)
                
        print(mejor_solucion)
                
    return mejor_solucion

# Función objetivo
def funcion_objetivo(solucion):
    x, y = solucion
    return -x**2 - 2*y**2 + 10*x - 3*y + 7

# Vecindario
def vecindario(solucion):
    x, y = solucion
    vecinos = []
    
    vecinos.append((x+1, y))
    vecinos.append((x-1, y))
    vecinos.append((x, y+1))
    vecinos.append((x, y-1))
    
    return vecinos

solucion_inicial = (0, 0)
longitud_tabu = 25
max_iter = 26

mejor_solucion = busqueda_tabu(solucion_inicial, funcion_objetivo, vecindario, longitud_tabu, max_iter)

print("La mejor solución encontrada es:", mejor_solucion)
print("El valor máximo encontrado es:", funcion_objetivo(mejor_solucion))
