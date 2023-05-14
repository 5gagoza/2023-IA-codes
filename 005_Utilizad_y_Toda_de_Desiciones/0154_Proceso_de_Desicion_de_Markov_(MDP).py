"""
El proceso de decisión de Markov, también conocido como cadena de Markov, es un modelo matemático utilizado para
describir secuencias de eventos en los que la probabilidad de que ocurra un evento futuro depende únicamente del evento
actual y no de los eventos pasados. Este proceso se basa en la propiedad de Markov, que establece que un estado futuro
solo depende del estado actual y no de cómo se llegó a ese estado.

En el contexto de un grafo, el proceso de decisión de Markov se puede utilizar para tomar decisiones en cada nodo del
grafo, donde la elección del próximo nodo depende únicamente del nodo actual. Cada nodo tiene una probabilidad asociada
a las transiciones hacia otros nodos.
"""

"""
Este código genera un grafo aleatorio utilizando nx.fast_gnp_random_graph de NetworkX y asigna probabilidades de
transición aleatorias a cada nodo. Luego, inicia el proceso de decisión seleccionando un nodo aleatorio y elige los
próximos nodos basándose en las probabilidades de transición hasta que se cumpla la condición de terminación, que en
este caso es cuando el nodo actual ya no tiene nuevos vecinos por los cuales pasar. En ese caso, se rompe el bucle y el
proceso de decisión de Markov finaliza.
"""

import random
import networkx as nx
from time import sleep

# Generar grafo aleatorio
num_nodes = 10
graph = nx.fast_gnp_random_graph(num_nodes, 0.25)

# Asignar probabilidades de transición aleatorias
transition_matrix = {}
for node in graph.nodes:
    neighbors = list(graph.neighbors(node))
    probabilities = [random.random() for _ in range(len(neighbors))]
    total = sum(probabilities)
    probabilities = [p / total for p in probabilities]
    transition_matrix[node] = dict(zip(neighbors, probabilities))

# Definir estado inicial
current_node = random.choice(list(graph.nodes))

# Iterar en el proceso de decisión
while True:
    sleep(0.5)
    print("Current node:", current_node)

    # Obtener probabilidades de transición del nodo actual
    probabilities = transition_matrix[current_node]
    next_node = random.choices(list(probabilities.keys()), list(probabilities.values()))[0]

    # Actualizar nodo actual
    current_node = next_node

    # Condición de terminación (puede personalizarse según tus necesidades)
    if len(list(graph.neighbors(current_node))) == 1:
        break
