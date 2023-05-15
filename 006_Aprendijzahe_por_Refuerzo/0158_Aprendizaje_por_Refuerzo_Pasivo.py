"""
El aprendizaje por refuerzo pasivo es un enfoque en el aprendizaje automático donde un agente aprende observando las
acciones de otro agente, en lugar de interactuar directamente con el entorno. El agente pasivo se centra en aprender una
política óptima basada en las señales de refuerzo recibidas por el agente activo.

El aprendizaje por refuerzo pasivo se refiere a aprender de las acciones de otro agente, y en el contexto de la búsqueda
en grafos, puede ayudar a mejorar la eficiencia y calidad de las búsquedas al adaptar la estrategia del agente pasivo en
base a las acciones observadas
"""

"""
El código generará un grafo aleatorio, definirá un nodo de inicio y un nodo final, realizará la búsqueda utilizando el
aprendizaje por refuerzo pasivo y mostrará los resultados gráficamente.
"""

import networkx as nx
import matplotlib.pyplot as plt
import random


# Generar grafo aleatorio
def generar_grafo(num_nodos, num_aristas):
    G = nx.gnm_random_graph(num_nodos, num_aristas)
    return G


# Definir nodo de inicio y nodo final
def definir_nodos(G):
    inicio = random.choice(list(G.nodes()))
    final = random.choice(list(G.nodes()))
    while final == inicio:
        final = random.choice(list(G.nodes()))
    return inicio, final


# Actualizar tabla de valores de acción-estado
def actualizar_valores(tabla_valores, estado_anterior, accion_anterior, estado_actual, recompensa, tasa_aprendizaje,
                       factor_descuento):
    valor_anterior = tabla_valores[estado_anterior][accion_anterior]
    mejor_valor_actual = max(tabla_valores[estado_actual].values())
    nuevo_valor = valor_anterior + tasa_aprendizaje * (
                recompensa + factor_descuento * mejor_valor_actual - valor_anterior)
    tabla_valores[estado_anterior][accion_anterior] = nuevo_valor


# Selección de acción basada en la tabla de valores
def seleccionar_accion(tabla_valores, estado, epsilon):
    if random.uniform(0, 1) < epsilon:
        # Exploración: seleccionar una acción aleatoria
        acciones_posibles = list(tabla_valores[estado].keys())
        accion = random.choice(acciones_posibles)
    else:
        # Explotación: seleccionar la mejor acción según la tabla de valores
        mejor_accion = max(tabla_valores[estado], key=tabla_valores[estado].get)
        accion = mejor_accion
    return accion


# Busqueda utilizando aprendizaje por refuerzo pasivo
def busqueda_aprendizaje_reforzado(G, inicio, final, tasa_aprendizaje, factor_descuento, epsilon, num_iteraciones):
    # Crear tabla de valores de acción-estado
    tabla_valores = {}
    for nodo in G.nodes():
        tabla_valores[nodo] = {nodo: 0 for nodo in G.neighbors(nodo)}

    # Realizar búsqueda
    path = [inicio]
    current_node = inicio
    for _ in range(num_iteraciones):
        if current_node == final:
            break
        next_node = seleccionar_accion(tabla_valores, current_node, epsilon)
        path.append(next_node)
        recompensa = 1 if next_node == final else 0
        actualizar_valores(tabla_valores, current_node, next_node, next_node, recompensa, tasa_aprendizaje,
                           factor_descuento)
        current_node = next_node

    return path


# Mostrar el grafo y el camino encontrado
def mostrar_resultados(G, path):
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True)
    nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i + 1]) for i in range(len(path) - 1)], edge_color='r',
                           width=2)
    plt.show()

# Parámetros del grafo y del aprendizaje por refuerzo pasivo
num_nodos = 10
num_aristas = 15
tasa_aprendizaje = 0.1
factor_descuento = 0.9
epsilon = 0.2
num_iteraciones = 100

# Generar grafo aleatorio
grafo = generar_grafo(num_nodos, num_aristas)

# Definir nodo de inicio y nodo final
nodo_inicio, nodo_final = definir_nodos(grafo)

# Buscar camino utilizando aprendizaje por refuerzo pasivo
camino = busqueda_aprendizaje_reforzado(grafo, nodo_inicio, nodo_final, tasa_aprendizaje, factor_descuento, epsilon, num_iteraciones)

# Mostrar resultados gráficamente
mostrar_resultados(grafo, camino)
