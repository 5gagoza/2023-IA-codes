# -*- coding: utf-8 -*-
"""
Created on Fri May 12 20:47:45 2023

@author: carlo

Grafos de Planificación: GRAPHPLAN
Los grafos de planificación, como GRAPHPLAN, se utilizan para representar y resolver 
problemas de planificación. Aquí tienes un ejemplo básico de código utilizando la biblioteca 
"pygraphplan" para implementar la planificación utilizando GRAPHPLAN en Python:
    
"""

from pygraphplan import PlanningGraph

# Definir acciones y precondiciones/efectos
actions = {
    'abrir_caja': (['cerrado'], ['abierto']),
    'coger_objeto': (['abierto', 'no_cogido'], ['cogido']),
    'poner_objeto': (['abierto', 'cogido'], ['no_cogido'])
}

# Definir el estado inicial y objetivo
estado_inicial = {'cerrado': True, 'no_cogido': True}
objetivo = {'cogido': True}

# Crear el grafo de planificación
graph = PlanningGraph(actions)

# Expandir el grafo hasta encontrar una solución
solution = graph.search(estado_inicial, objetivo)

# Imprimir el plan
if solution is not None:
    for action in solution:
        print(action)
else:
    print("No se encontró una solución.")


"""
En este ejemplo, se definen las acciones junto con sus precondiciones y efectos en 
un diccionario. Luego, se crea un objeto de grafo de planificación y se busca una 
solución expandiendo el grafo hasta alcanzar un estado objetivo. Si se encuentra una 
solución, se imprime el plan de acciones para alcanzar el objetivo.
"""