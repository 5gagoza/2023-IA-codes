"""
Diferentes tipos de redes neuronales con características y aplicaciones
especificas y diferentes 
"""

import numpy as np

class HammingNetwork:
    def __init__(self, input_size, output_size, weights):
        self.input_size = input_size
        self.output_size = output_size
        self.weights = weights

    def predict(self, X):
        activations = np.dot(X, self.weights.T)
        winner_indices = np.argmax(activations, axis=1)
        return winner_indices

# Ejemplo de uso
# Datos de entrada
X = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# Matriz de pesos predefinida para una red de Hamming 4x2
weights = np.array([
    [1, -1, 1, -1],
    [-1, 1, -1, 1]
])

# Instanciar la red neuronal de Hamming
network = HammingNetwork(input_size=4, output_size=2, weights=weights)

# Realizar predicciones
predictions = network.predict(X)

# Imprimir los resultados
print("Predicciones:", predictions)

