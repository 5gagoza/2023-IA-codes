"""
Computación Neuronal:
La computación neuronal se refiere al estudio de los 
procesos computacionales inspirados en el funcionamiento 
del cerebro humano. Se basa en la idea de que las neuronas 
y sus interconexiones pueden ser modeladas y utilizadas 
para realizar tareas de procesamiento de información.

"""

""" Implementa una red neuronal simple basada en la computación neuronal
con el objetivo de realizar una operación lógica XOR,"""

import numpy as np

# Función de activación sigmoidal
def sigmoid(x): #Función para introducción a la no linealidad
    return 1 / (1 + np.exp(-x))

# Clase de la red neuronal
class NeuralNetwork:
    def __init__(self):
        # Inicialización de los pesos aleatoriamente
        self.weights = np.random.rand(2)
        # Inicialización del sesgo a cero
        self.bias = 0
    
    # Función de propagación hacia adelante
    def forward(self, x):
        # Calcula la suma ponderada de las entradas y los pesos
        z = np.dot(self.weights, x) + self.bias
        # Aplica la función de activación sigmoidal al resultado
        a = sigmoid(z)
        return a
    
    # Función de entrenamiento
    def train(self, X, y, epochs):
        for epoch in range(epochs):
            for x, target in zip(X, y):
                # Realiza la propagación hacia adelante para obtener la predicción
                output = self.forward(x)
                # Calcula el error
                error = target - output
                # Actualiza los pesos y el sesgo
                self.weights += error * x
                self.bias += error
    
    # Función de predicción
    def predict(self, x):
        # Realiza la propagación hacia adelante para obtener la predicción
        output = self.forward(x)
        # Redondea la salida para obtener la clase (0 o 1)
        prediction = np.round(output)
        return prediction

# Ejemplo de uso
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

# Crear y entrenar la red neuronal
nn = NeuralNetwork()
nn.train(X, y, epochs=1000)

# Realizar predicciones
for x in X:
    prediction = nn.predict(x)
    print("Entrada:", x, "Predicción:", prediction)
