#Supongamos que queremos simular un proceso de Markov de segundo orden que modela el estado del clima (soleado, nublado, lluvioso) utilizando una matriz de transición.

import numpy as np

# Definir la matriz de transición de segundo orden
transiciones = np.array([[[0.7, 0.2, 0.1],
                         [0.4, 0.3, 0.3],
                         [0.2, 0.2, 0.6]],

                        [[0.5, 0.3, 0.2],
                         [0.2, 0.6, 0.2],
                         [0.1, 0.3, 0.6]],

                        [[0.6, 0.3, 0.1],
                         [0.3, 0.4, 0.3],
                         [0.2, 0.2, 0.6]]])

# Definir el estado inicial
estado_actual = np.random.choice([0, 1, 2])

# Simular el proceso de Markov de segundo orden
secuencia_estados = [estado_actual]

for _ in range(10):
    estado_anterior = secuencia_estados[-1]
    prob_transicion = transiciones[estado_anterior]
    estado_siguiente = np.random.choice([0, 1, 2], p=prob_transicion)
    secuencia_estados.append(estado_siguiente)

print("Secuencia de estados generada:", secuencia_estados)
