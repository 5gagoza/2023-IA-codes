"""
la teoría de la utilidad busca optimizar un camino teniendo en cuenta los valores de utilidad asignados a los nodos o
aristas del grafo, con el objetivo de maximizar la utilidad total en lugar de minimizar un costo específico.

Esto se logra asignando valores de utilidad a los nodos o aristas del grafo, y luego calculando la utilidad acumulada a
lo largo de un camino determinado. La utilidad puede representar cualquier criterio deseado, como la velocidad, el
costo, la confiabilidad, etc.
"""

"""
En este ejemplo, se utiliza el algoritmo de Dijkstra para encontrar los caminos más útiles desde un nodo inicial en un
grafo. La función calculate_utility se utiliza para asignar una utilidad a cada arista (en este caso, se utiliza el
inverso del peso de la arista como utilidad).

El algoritmo de Dijkstra se modifica ligeramente para calcular la utilidad acumulada a lo largo del camino y
actualizar las distancias en consecuencia. Al final, se obtiene un diccionario distances que contiene las distancias
más útiles desde el nodo inicial a cada uno de los nodos del grafo.
"""

import heapq


def dijkstra(graph, start):
    # Inicializar las estructuras de datos
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        # Si ya hemos encontrado un camino más corto a este nodo, ignorarlo
        if current_dist > distances[current_node]:
            continue

        # Explorar los vecinos del nodo actual
        for neighbor, weight in graph[current_node].items():
            utility = calculate_utility(weight)  # Calcular la utilidad para la arista

            # Calcular la utilidad acumulada para el vecino
            neighbor_utility = distances[current_node] + utility

            # Si encontramos un camino más útil hacia el vecino, actualizar la distancia y agregarlo a la cola
            if neighbor_utility < distances[neighbor]:
                distances[neighbor] = neighbor_utility
                heapq.heappush(queue, (neighbor_utility, neighbor))

    return distances


# Función de ejemplo para calcular la utilidad de una arista
def calculate_utility(weight):
    # Aquí puedes implementar tu propia función de cálculo de utilidad según tus necesidades
    return 1 / weight


# Ejemplo de uso
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 3, 'E': 5},
    'C': {'D': 1},
    'D': {'E': 1},
    'E': {}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print("Distancias más útiles desde el nodo inicial:")
for node, distance in distances.items():
    print(f"Nodo: {node}, Distancia: {distance}")
