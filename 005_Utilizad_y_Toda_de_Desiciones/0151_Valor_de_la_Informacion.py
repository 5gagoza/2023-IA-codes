"""
El valor de la información en la búsqueda en grafos es una medida que nos permite evaluar y priorizar los nodos o
aristas más relevantes en función de ciertos criterios, lo que facilita la toma de decisiones durante la exploración
del grafo.
"""

"""
Este código crea un grafo de ejemplo, asigna valores de información a cada nodo, realiza una búsqueda basada en el
valor de información
"""

import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo de ejemplo
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (5, 6)])

# Definir valores de información para los nodos
valores_informacion = {1: 0.8, 2: 0.5, 3: 0.6, 4: 0.9, 5: 0.7, 6: 0.4}


# Función para obtener el valor de información de un nodo
def obtener_valor_informacion(nodo):
    return valores_informacion.get(nodo, 0)


# Función para visualizar el grafo con los valores de información y el camino resaltado
def visualizar_grafo_con_valores_informacion(grafo, valores, camino):
    pos = nx.spring_layout(grafo)
    node_colors = [valores.get(nodo, 0) for nodo in grafo.nodes()]
    node_sizes = [val * 1000 for val in node_colors]
    edge_colors = ['red' if (u, v) in zip(camino, camino[1:]) else 'black' for u, v in grafo.edges()]

    nx.draw(grafo, pos, with_labels=True, node_size=node_sizes, node_color=node_colors, edge_color=edge_colors,
            cmap='cool')
    labels = nx.get_node_attributes(grafo, 'label')
    nx.draw_networkx_labels(grafo, pos, labels=labels)

    # Mostrar los valores de información junto a los nodos
    for node, (x, y) in pos.items():
        plt.text(x, y + 0.05, f"Val: {valores.get(node, 0)}", ha='center', fontsize=8)

    plt.show()


# Asignar etiquetas de nodo con los valores de información
nx.set_node_attributes(G, valores_informacion, 'label')

# Visualizar el grafo inicial con los valores de información
visualizar_grafo_con_valores_informacion(G, valores_informacion, [])

# Realizar una búsqueda en el grafo utilizando el valor de información
inicio = 1
camino = [inicio]
valor_total = 0

while camino:
    nodo_actual = camino[-1]
    vecinos = list(G[nodo_actual])
    valores = [obtener_valor_informacion(nodo) for nodo in vecinos]

    if not valores:
        break

    mejor_vecino = vecinos[valores.index(max(valores))]
    camino.append(mejor_vecino)
    valor_total += obtener_valor_informacion(mejor_vecino)

# Visualizar el camino obtenido y su valor total
print("Camino:", camino)
print("Valor total de información:", valor_total)

# Visualizar el grafo con el camino resaltado
visualizar_grafo_con_valores_informacion(G, valores_informacion, camino)
