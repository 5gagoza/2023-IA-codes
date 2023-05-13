"""
El perceptrón es uno de los modelos más simples de redes neuronales. 
Es una red neuronal de una sola capa con una única neurona.
ADALINE (Adaptive Linear Neuron) y MADALINE (Multiple ADALINE) son 
extensiones del perceptrón que permiten el aprendizaje de clasificaciones 
lineales con regresión continua. Estos modelos se basan en el ajuste de los pesos de las
conexiones en función del error cometido y el uso de una función de activación lineal.

""" 

"""Implementa el Perceptrón, ADALINE y MADALINE utilizando AND Y OR"""

import numpy as np

# Clase Perceptrón
class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.zeros(input_size)
        self.learning_rate = learning_rate
    
    def predict(self, x): #Creación de la predicción
        # Calcula el producto punto entre los pesos y las entradas
        activation = np.dot(self.weights, x)
        # Aplica la función de activación (en este caso, el escalón)
        return 1 if activation >= 0 else 0
    
    def train(self, X, y, epochs): #Creación del entrenamiento
        for _ in range(epochs):
            for x, target in zip(X, y):
                # Realiza la predicción
                prediction = self.predict(x)
                # Calcula el error
                error = target - prediction
                # Actualiza los pesos
                self.weights += self.learning_rate * error * x

# Clase ADALINE
class ADALINE:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.zeros(input_size)
        self.learning_rate = learning_rate
    
    def predict(self, x):
        # Calcula el producto punto entre los pesos y las entradas
        activation = np.dot(self.weights, x)
        # No aplica función de activación
        return activation
    
    def train(self, X, y, epochs):
        for _ in range(epochs):
            for x, target in zip(X, y):
                # Realiza la predicción
                prediction = self.predict(x)
                # Calcula el error
                error = target - prediction
                # Actualiza los pesos
                self.weights += self.learning_rate * error * x

# Clase MADALINE
class MADALINE:
    def __init__(self, input_size, output_size, learning_rate=0.1):
        self.weights = np.zeros((output_size, input_size))
        self.learning_rate = learning_rate
    
    def predict(self, x):
        # Calcula el producto punto entre los pesos y las entradas
        activation = np.dot(self.weights, x)
        # Aplica la función de activación (en este caso, el escalón)
        return np.where(activation >= 0, 1, -1)
    
    def train(self, X, y, epochs):
        for _ in range(epochs):
            for x, target in zip(X, y):
                # Realiza la predicción
                prediction = self.predict(x)
                # Calcula el error
                error = target - prediction
                # Actualiza los pesos
                self.weights += self.learning_rate * np.outer(error, x)

# Ejemplo de uso
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])
y_or = np.array([0, 1, 1, 1])

# Perceptrón
perceptron = Perceptron(input_size=2)
perceptron.train(X, y_and, epochs=10)
for x in X:
    prediction = perceptron.predict(x)
    print(f"Entrada: {x}, Predicción (AND): {prediction}")

# ADALINE
adaline = ADALINE(input_size=2)
adaline.train(X, y_or, epochs=10)
for x in X:
    prediction = adaline.predict(x)
    print(f"Entrada: {x}, Predicción (OR): {prediction}")

# MADALINE
madaline = MADALINE(input_size=2, output_size=1)
madaline.train(X, y_and, epochs=10)
for x in X:
    prediction = madaline.predict(x)
    print(f"Entrada: {x}, Predicción (AND): {prediction}")


