"""
En la búsqueda de la política, se trata de encontrar la mejor secuencia de acciones para alcanzar un objetivo en un
grafo o un conjunto de nodos interconectados. Esta técnica se utiliza en problemas donde hay múltiples posibles caminos
para llegar a un objetivo y se busca encontrar la secuencia más óptima.

La búsqueda de la política se basa en la evaluación de diferentes caminos mediante algoritmos de búsqueda, como el
algoritmo A* o el algoritmo de búsqueda en anchura (BFS). Estos algoritmos exploran los nodos y las aristas del grafo,
evaluando diferentes opciones y determinando cuál es la más prometedora en términos de alcanzar el objetivo

En resumen, la búsqueda de la política en el ámbito de búsqueda en grafos consiste en encontrar la mejor secuencia de
acciones para alcanzar un objetivo evaluando diferentes caminos y utilizando heurísticas para guiar la exploración.
"""

"""
En este ejemplo, se utiliza la función gnp_random_graph de NetworkX para generar un grafo aleatorio con 10 nodos y una
probabilidad de conexión del 0.3. Luego, se elige un nodo de inicio y un nodo objetivo al azar.

Después de encontrar el camino utilizando la función buscar_politica, se muestra el camino resultante en la consola.
Luego, se utiliza NetworkX y Matplotlib para visualizar el grafo y resaltar el camino encontrado en rojo. El resultado
se muestra en una ventana gráfica.
"""

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import random

def buscar_politica(grafo, inicio, objetivo):
    camino = {}
    cola = deque()
    cola.append(inicio)
    while cola:
        nodo_actual = cola.popleft()
        if nodo_actual == objetivo:
            break
        for vecino in grafo[nodo_actual]:
            if vecino not in camino:
                camino[vecino] = nodo_actual
                cola.append(vecino)
    ruta = []
    nodo = objetivo
    while nodo != inicio:
        ruta.append(nodo)
        nodo = camino[nodo]
    ruta.append(inicio)
    ruta.reverse()
    return ruta

# Crear un grafo aleatorio
grafo = nx.gnp_random_graph(10, 0.3, directed=False)
inicio = random.choice(list(grafo.nodes))
objetivo = random.choice(list(grafo.nodes))
while inicio == objetivo:
    objetivo = random.choice(list(grafo.nodes))

# Encontrar el camino utilizando la búsqueda de política
politica = buscar_politica(grafo, inicio, objetivo)
print("Camino:", politica)

# Visualizar el grafo y el camino resultante
pos = nx.spring_layout(grafo)
nx.draw(grafo, pos, with_labels=True, node_color='lightblue')
nx.draw_networkx_nodes(grafo, pos, nodelist=politica, node_color='red')
nx.draw_networkx_edges(grafo, pos, edgelist=[(politica[i], politica[i+1]) for i in range(len(politica)-1)], edge_color='red', width=2)
plt.title("Grafo y camino resultante")
plt.show()
