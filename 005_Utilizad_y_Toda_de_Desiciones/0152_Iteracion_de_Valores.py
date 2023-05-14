"""
La iteración de valores en la búsqueda en grafos es un enfoque utilizado para recorrer y buscar elementos en un grafo.
Consiste en explorar el grafo de manera gradual, comenzando desde un nodo inicial y expandiendo iterativamente a sus
vecinos.

El proceso de iteración implica mantener una lista de nodos visitados y una cola de nodos por visitar. En cada
iteración, se toma un nodo de la cola, se marca como visitado y se examinan sus vecinos. Los vecinos no visitados se
agregan a la cola para su posterior exploración. Este proceso se repite hasta que se encuentre el elemento buscado o
hasta que se hayan visitado todos los nodos accesibles desde el nodo inicial.

La iteración de valores en la búsqueda en grafos puede implementarse utilizando estructuras de datos como colas o pilas.
Dependiendo de la estructura utilizada y del orden en que se visitan los nodos, se pueden obtener diferentes estrategias
de búsqueda, como la búsqueda en anchura (BFS) o la búsqueda en profundidad (DFS).
"""

"""
El grafo se define como un diccionario de listas de adyacencia. La función bfs implementa la búsqueda en anchura y
devuelve un valor booleano que indica si se encontró el objetivo.

El grafo se dibujará utilizando el trazado del grafo de NetworkX. Los nodos se etiquetarán con sus nombres y se
colorearán de azul claro si son el nodo de inicio, verde claro si es el nodo objetivo y de gris claro en caso contrario.
Los bordes se colorearán de negro si el objetivo se encuentra durante la búsqueda en anchura y de gris claro en caso
contrario.
"""

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import random


def bfs(graph, start_node, target):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node == target:
            return True

        visited.add(node)
        neighbors = graph[node]

        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)

    return False


# Generar un grafo aleatorio utilizando NetworkX
num_nodes = 10  # Número de nodos
prob = 0.3  # Probabilidad de crear un borde entre dos nodos
random_graph = nx.fast_gnp_random_graph(num_nodes, prob, directed=True)

# Convertir el grafo aleatorio en un diccionario de listas de adyacencia
graph = {str(node): [str(neighbor) for neighbor in neighbors] for node, neighbors in random_graph.adj.items()}

start_node = random.choice(list(graph.keys()))
target_node = random.choice(list(graph.keys()))

# Crear el grafo dirigido utilizando NetworkX
G = nx.DiGraph(graph)

# Obtener el trazado del grafo
pos = nx.spring_layout(G)

# Etiquetas de nodos
labels = {node: node for node in G.nodes}

# Colores de nodos
node_colors = ['lightblue' if node == start_node else 'lightgreen' if node == target_node else 'lightgray' for node in G.nodes]

# Colores de bordes
edge_colors = ['black' if bfs(graph, start_node, target_node) else 'lightgray' for _, _ in G.edges]

# Dibujar el grafo
nx.draw_networkx(G, pos, labels=labels, node_color=node_colors, edge_color=edge_colors, arrows=True)
plt.axis('off')
plt.show()

