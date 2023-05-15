import networkx as nx
import matplotlib.pyplot as plt
import time

def prim(G, source):
    # Inicializar variables
    visitados = set([source])
    pesos = {}
    arbol = nx.Graph()
    arbol.add_node(source)

    # Inicializar pesos de todas las aristas como infinito
    for u, v in G.edges():
        pesos[(u, v)] = float('inf')

    # Asignar pesos reales a las aristas que existen en el grafo
    for u, v, peso in G.edges(data=True):
        pesos[(u, v)] = peso['weight']
        pesos[(v, u)] = peso['weight']

    pos = nx.spring_layout(G)
    # Iterar hasta que se hayan visitado todos los nodos
    while len(visitados) < len(G.nodes()):
        # Encontrar la arista de menor peso que conecta un nodo visitado y uno no visitado
        u, v = min([(u, v) for (u, v) in pesos if u in visitados and v not in visitados], key=lambda x: pesos[x])
        peso = pesos[(u, v)]

        # Agregar el nodo no visitado al conjunto de visitados
        visitados.add(v)

        # Agregar la arista al árbol
        arbol.add_edge(u, v, weight=peso)

        # Imprimir el paso actual
        print("Nodo agregado: {}, Arista agregada: ({}, {}) con peso {}".format(v, u, v, peso))
        plt.clf()
        plt.plot()
        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
        nx.draw_networkx_edges(arbol, pos, edge_color='r', width=2)
        plt.pause(0.5)

    return arbol

# Crear grafo
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'H', weight=8)
G.add_edge('B', 'C', weight=8)
G.add_edge('B', 'H', weight=11)
G.add_edge('C', 'D', weight=7)
G.add_edge('C', 'I', weight=2)

arbol_par = prim(G, 'A')

'''
¿Qué es? Algoritmo para encontrar el árbol de Mínimo Coste de un grafo no dirigido.
¿Para qué sirve? En la resolución de problemas de optimización de redes, como en la
planificación de rutas de transporte o en la distribución de suministros.
¿Cómo se implementa en el mundo? En sistemas de ruteo de paquetes en redes de comunicaciones, 
en la gestión de infraestructuras de suministro de energía, agua o gas, entre otros.
¿Cómo lo implementarías en tu vida? Para, eliminar o posponer actividades que puedan ser innecesarias.
¿Cómo lo implementarías en tu trabajo o tu trabajo de ensueño? Optimizartiempos asignados para actividades.
'''