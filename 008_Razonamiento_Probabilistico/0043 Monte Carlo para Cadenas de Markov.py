import numpy as np

# Definir la matriz de transición de la cadena de Markov
transiciones = np.array([[0.6, 0.3, 0.1],
                         [0.2, 0.5, 0.3],
                         [0.3, 0.1, 0.6]])

# Definir la cantidad de pasos a simular
num_pasos = 10

# Definir el estado inicial
estado_actual = 0  # 0: Soleado, 1: Nublado, 2: Lluvioso

# Simular la cadena de Markov utilizando el método de Monte Carlo
secuencia_estados = [estado_actual]

for _ in range(num_pasos):
    estado_siguiente = np.random.choice([0, 1, 2], p=transiciones[estado_actual])
    secuencia_estados.append(estado_siguiente)
    estado_actual = estado_siguiente

print("Secuencia de estados generada:", secuencia_estados)
