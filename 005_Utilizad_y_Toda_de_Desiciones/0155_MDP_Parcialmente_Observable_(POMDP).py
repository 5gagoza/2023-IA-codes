"""
En resumen, la principal diferencia entre un MDP y un POMDP radica en la información disponible para el agente al tomar
decisiones. En un MDP, el agente conoce el estado actual de manera completa y precisa, mientras que en un POMDP, el
agente solo tiene acceso a observaciones parciales del estado y debe mantener una creencia o estimación sobre el estado
real.

En un POMDP, las observaciones parciales y la incertidumbre sobre el estado pueden complicar la toma de decisiones
óptimas. Se requieren enfoques específicos, como algoritmos de planificación y aprendizaje basados en POMDP, para
abordar la toma de decisiones en este tipo de entornos. Estos algoritmos generalmente involucran la construcción y
actualización de creencias sobre el estado, así como la consideración de incertidumbre y recompensas esperadas en el
proceso de toma de decisiones.
"""

"""
El problema de los POMDPs es considerablemente más complejo que el de los MDPs debido a la incertidumbre inherente al no
conocer completamente el estado. Implementar un algoritmo completo para resolver POMDPs es una tarea compleja y requiere
algoritmos de planificación y aprendizaje especializados.

A continuación, se muestra un código básico que ilustra la estructura general de un POMDP y cómo se puede actualizar la
creencia del agente en función de las observaciones parciales. Sin embargo, este código no resolverá el POMDP completo,
ya que esto implicaría considerar todos los estados, acciones y recompensas posibles, así como implementar algoritmos de
planificación y aprendizaje más sofisticados.
"""

import random
import networkx as nx
from time import sleep

# Generar grafo aleatorio con al menos un nodo sin vecinos
num_nodes = 10
graph = None
while True:
    graph = nx.fast_gnp_random_graph(num_nodes, 0.25)  # Ajusta el valor de p según sea necesario
    isolated_nodes = [node for node in graph.nodes if len(list(graph.neighbors(node))) == 0]
    if len(isolated_nodes) > 0:
        break

# Definir estado inicial y creencia inicial
current_state = random.choice(list(graph.nodes))
belief = {node: 1 / num_nodes for node in graph.nodes}

# Definir funciones de transición y observación aleatorias
def transition_model(current_state, action):
    neighbors = list(graph.neighbors(current_state))
    return random.choice(neighbors)

def observation_model(current_state):
    return current_state

# Iterar en el proceso de decisión parcialmente observable
while True:
    sleep(0.5)
    print("Current state:", current_state)
    print("Belief:", belief)

    # Tomar acción basada en la creencia actual
    action = random.choice(list(graph.neighbors(current_state)))

    # Observar el estado parcialmente
    observation = observation_model(current_state)

    # Actualizar la creencia utilizando el modelo de transición y observación
    new_belief = {}
    for node in graph.nodes:
        prior = belief[node]
        likelihood = 1 if node == observation else 0.1  # Simplified observation model
        transition_prob = 1 if node == transition_model(current_state, action) else 0.1  # Simplified transition model
        new_belief[node] = prior * likelihood * transition_prob
    total_belief = sum(new_belief.values())
    belief = {node: new_belief[node] / total_belief for node in graph.nodes}

    # Actualizar el estado actual en función de la acción tomada
    current_state = transition_model(current_state, action)

    # Condición de terminación (llegar a un nodo sin vecinos)
    if len(list(graph.neighbors(current_state))) == 1:
        break
