"""
La separabilidad lineal se refiere a la capacidad de una 
red neuronal para dividir un conjunto de datos en diferentes 
clases utilizando una función de decisión lineal. Si los datos 
son linealmente separables, es posible encontrar una combinación 
lineal de los pesos y las entradas que permita separar correctamente las clases.
"""
""" Clasificacion de datos lineales en un perceptron """
import numpy as np
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

# Generar datos de ejemplo linealmente separables
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0,
                           n_clusters_per_class=1, random_state=42)

# Visualizar los datos generados
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Linearly Separable Data')
plt.show()

# Clase para la red neuronal
class NeuralNetwork: #Representación de la red neuronal
    def __init__(self, input_size):
        self.weights = np.random.randn(input_size)
        self.bias = np.random.randn()
    
    def predict(self, X): #Calcular la salida de la red
        linear_output = np.dot(X, self.weights) + self.bias
        activated_output = self.activation(linear_output)
        return activated_output
    
    def activation(self, x):
        # Función de activación sigmoidal
        return 1 / (1 + np.exp(-x))
    
    def train(self, X, y, learning_rate, epochs): #Metodo de entrenamiento
        for _ in range(epochs):
            for xi, target in zip(X, y):
                prediction = self.predict(xi)
                error = target - prediction
                self.weights += learning_rate * error * xi
                self.bias += learning_rate * error

# Crear una instancia de la red neuronal
nn = NeuralNetwork(input_size=2)

# Entrenar la red neuronal
nn.train(X, y, learning_rate=0.1, epochs=100)

# Visualizar los datos y la frontera de decisión aprendida
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Linearly Separable Data with Decision Boundary')
x_boundary = np.linspace(np.min(X[:, 0]), np.max(X[:, 0]), 100)
y_boundary = -(nn.weights[0] * x_boundary + nn.bias) / nn.weights[1]
plt.plot(x_boundary, y_boundary, color='red')
plt.show()
