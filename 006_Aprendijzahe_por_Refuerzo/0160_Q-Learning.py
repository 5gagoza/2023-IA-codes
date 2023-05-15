"""
el Q-Learning es un algoritmo de aprendizaje por refuerzo que se utiliza para resolver problemas de toma de decisiones
en entornos desconocidos. En la búsqueda en grafos, el Q-Learning se aplica para encontrar la ruta óptima de menor costo
en un grafo ponderado, aprendiendo los valores Q que representan la utilidad esperada de tomar acciones en diferentes
estados.
"""

"""
Este código genera un grafo aleatorio utilizando la biblioteca Networkx y luego aplica el algoritmo Q-Learning para
aprender los valores de Q. Luego, utiliza la biblioteca Matplotlib para visualizar el grafo y resaltar las conexiones
más probables según los valores de Q.
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Generar un grafo aleatorio utilizando la biblioteca Networkx
num_nodes = 5
graph = nx.erdos_renyi_graph(num_nodes, 0.5)

# Convertir el grafo en una matriz de adyacencia
adj_matrix = nx.adjacency_matrix(graph).todense()

# Definir las recompensas asociadas a cada acción
rewards = np.random.randint(-10, 10, size=(num_nodes, num_nodes))
np.fill_diagonal(rewards, 0)

# Inicializar la matriz Q con valores arbitrarios
Q = np.zeros_like(adj_matrix, dtype=float)

# Definir los hiperparámetros
learning_rate = 0.8
discount_factor = 0.9
num_episodes = 100

# Ejecutar el algoritmo Q-Learning
for episode in range(num_episodes):
    current_state = np.random.randint(0, num_nodes)
    while True:
        # Elegir una acción basada en el valor de Q y una política epsilon-greedy
        epsilon = 0.3
        if np.random.uniform(0, 1) < epsilon:
            action = np.random.choice(np.where(adj_matrix[current_state] == 1)[0])
        else:
            action = np.argmax(Q[current_state])

        # Actualizar el valor de Q
        next_state = action
        Q[current_state, action] = (1 - learning_rate) * Q[current_state, action] + \
                                   learning_rate * (rewards[current_state, action] + \
                                                    discount_factor * np.max(Q[next_state]))

        # Mover al siguiente estado
        current_state = next_state
        if current_state == 3:  # Estado objetivo es el estado 3
            break

# Imprimir la matriz Q resultante
print("Matriz Q resultante:")
print(Q)

# Visualizar el grafo y las conexiones más probables según los valores de Q
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(graph)
nx.draw_networkx_nodes(graph, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_labels(graph, pos, font_color='black')
for i in range(num_nodes):
    for j in range(num_nodes):
        if adj_matrix[i, j] == 1:
            prob = Q[i, j] / np.sum(Q[i])  # Calcular la probabilidad de elegir esa conexión
            nx.draw_networkx_edges(graph, pos, edgelist=[(i, j)], width=prob * 2, alpha=0.7, edge_color='red')
plt.axis('off')
plt.title('Grafo y conexiones más probables')
plt.show()
