import networkx as nx
import matplotlib.pyplot as plt

def kruskal(G, minimum=True):
    # Creamos un grafo vacío T
    T = nx.Graph()
    # Ordenamos las aristas por su peso
    edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    # Creamos un conjunto para cada vértice (inicialmente, cada vértice es su propio conjunto)
    sets = {v: set([v]) for v in G.nodes()}
    # Recorremos las aristas en orden ascendente de peso
    for u, v, w in edges:
        # Si los extremos de la arista pertenecen a conjuntos distintos
        if sets[u] != sets[v]:
            # Agregamos la arista al árbol
            T.add_edge(u, v, weight=w['weight'])
            # Unimos los conjuntos de u y v
            sets[u] |= sets[v]
            sets[v] = sets[u]
            # Si ya hemos agregado suficientes aristas, salimos del bucle
            if len(T.edges()) == len(G.nodes()) - 1:
                break
    # Si estamos buscando el Árbol de Máximo coste, invertimos las aristas
    if not minimum:
        T = nx.create_empty_copy(G)
        for u, v, w in T.edges(data=True):
            T.add_edge(u, v, weight=-w['weight'])
    return T

def simulate_kruskal(G, minimum=True):
    # Creamos un grafo vacío T
    T = nx.Graph()
    # Ordenamos las aristas por su peso
    edges = sorted(G.edges(data=True), key=lambda x: x[2]['weight'])
    # Creamos un conjunto para cada vértice (inicialmente, cada vértice es su propio conjunto)
    sets = {v: set([v]) for v in G.nodes()}
    # Imprimimos el grafo original
    print("Grafo original:")
    print(G.edges(data=True))
    nx.draw(G, with_labels=True)
    plt.show()
    # Recorremos las aristas en orden ascendente de peso
    for i, (u, v, w) in enumerate(edges):
        # Si los extremos de la arista pertenecen a conjuntos distintos
        if sets[u] != sets[v]:
            # Agregamos la arista al árbol
            T.add_edge(u, v, weight=w['weight'])
            # Unimos los conjuntos de u y v
            sets[u] |= sets[v]
            sets[v] = sets[u]
            # Imprimimos las aristas agregadas hasta este momento
            print(f"Paso {i+1}:")
            print(T.edges(data=True))
            nx.draw(T, with_labels=True)
            edge_labels = nx.get_edge_attributes(T, 'weight')
            nx.draw_networkx_edge_labels(T, pos=nx.spring_layout(T), edge_labels=edge_labels)
            plt.show()
            # Si ya hemos agregado suficientes aristas, salimos del bucle
            if len(T.edges()) == len(G.nodes()) - 1:
                break
    # Si estamos buscando el Árbol de Máximo coste, invertimos las aristas
    if not minimum:
        T = nx.create_empty_copy(G)
        for u, v, w in T.edges(data=True):
            T.add_edge(u, v, weight=-w['weight'])
    return T

# Creamos un grafo de ejemplo
G = nx.Graph()
G.add_edge('A', 'B', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=4)
G.add_edge('C', 'D', weight=5)

# Simulamos el algoritmo de Kruskal para obtener el Árbol de Mínimo coste
simulate_kruskal(G)

# Simulamos el algoritmo de Kruskal para obtener el Árbol de Máximo coste
simulate_kruskal(G, minimum=False)

'''
¿Qué es? Algoritmo para encontrar el árbol de Mínimo Coste de un grafo no dirigido.
¿Para qué sirve? En la resolución de problemas de optimización de redes, como en la planificación
de rutas de transporte o en la distribución de suministros.
¿Cómo se implementa en el mundo? En sistemas de enrutamiento de paquetes en redes de comunicaciones, 
en la gestión de infraestructuras de suministro de energía, agua o gas, en la selección de características 
importantes en la clasificación de datos, entre otros.
¿Cómo lo implementarías en tu vida? Simplificando las actividades que pueda tener planeadas, para tomarlo como
una opcion de como hacer las actividades.
¿Cómo lo implementarías en tu trabajo o tu trabajo de ensueño? Simplificando rutinas de trabajo.
'''