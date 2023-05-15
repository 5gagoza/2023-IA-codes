import networkx as nx
import matplotlib.pyplot as plt
import time

def dijkstra(G, source):
    # Inicialización de las estructuras de datos
    dist = {v: float('inf') for v in G.nodes()}
    dist[source] = 0
    visited = set()

    # Dibujar el grafo inicial
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.pause(0.5)

    while len(visited) < len(G.nodes()):
        # Seleccionar el nodo no visitado con la distancia más corta
        u = min((dist[v], v) for v in G.nodes() if v not in visited)[1]
        visited.add(u)

        # Actualizar las distancias de los vecinos no visitados
        for v in G.neighbors(u):
            if v not in visited:
                alt = dist[u] + G[u][v]['weight']
                if alt < dist[v]:
                    dist[v] = alt

        # Dibujar el grafo actualizado
        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): G[u][v]['weight'] for (u, v) in G.edges()})
        nx.draw_networkx_nodes(G, pos, nodelist=visited, node_color='g')
        nx.draw_networkx_nodes(G, pos, nodelist=[u], node_color='r')
        nx.draw_networkx_labels(G, pos, labels={u: str(dist[u]) for u in dist})
        plt.pause(0.5)

    return dist

# Crear el grafo de ejemplo
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])
G.add_weighted_edges_from([('A', 'B', 2), ('A', 'C', 3), ('B', 'C', 1), ('B', 'D', 2),
                           ('C', 'D', 1), ('C', 'E', 4), ('D', 'E', 2), ('D', 'F', 3),
                           ('E', 'F', 1)])

# Ejecutar el algoritmo de Dijkstra con el nodo 'A' como origen
dijkstra(G, 'A')

# Mostrar la figura final
plt.show()

'''
¿Qué es? Dijkstra es un algoritmo de búsqueda de caminos más cortos en un grafo ponderado.
¿Para qué sirve? Sirve para encontrar la ruta más corta entre dos nodos en un grafo, o para 
encontrar la ruta más corta desde un nodo dado a todos los demás nodos en el grafo.
¿Cómo se implementa en el mundo? Dijkstra se utiliza en muchas aplicaciones en la vida real, 
como en la planificación de rutas en aplicaciones de mapas, en redes de telecomunicaciones, en 
algoritmos de enrutamiento de redes informáticas, en la programación lineal, entre otros.
¿Cómo lo implementarías en tu vida? Podría utilizar el algoritmo de Dijkstra para planificar 
la ruta más corta entre dos lugares en un mapa, como en una aplicación de navegación.
¿Cómo lo implementarías en tu trabajo o tu trabajo de ensueño? En mi trabajo o trabajo de ensueño, 
podría utilizar el algoritmo de Dijkstra en el diseño y análisis de redes de telecomunicaciones para 
encontrar la ruta más corta entre dos puntos en una red, o para planificar la ruta de transmisión más eficiente 
para los datos.
'''