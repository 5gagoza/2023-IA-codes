"""
La retropropagación del error es un algoritmo utilizado para 
entrenar redes neuronales multicapa. Consiste en propagar hacia 
atrás el error calculado en la capa de salida de la red hacia 
las capas anteriores, ajustando los pesos de las conexiones en 
función del error. Este algoritmo permite que la red mejore su 
capacidad de hacer predicciones a medida que se entrena con un conjunto de datos.
"""
import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Inicialización de los pesos de forma aleatoria
        self.weights1 = np.random.randn(self.input_size, self.hidden_size)
        self.weights2 = np.random.randn(self.hidden_size, self.output_size)

    def sigmoid(self, x):
        # Función de activación sigmoide
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        # Derivada de la función de activación sigmoide
        return x * (1 - x)

    def forward(self, X):
        # Propagación hacia adelante
        self.hidden_layer = self.sigmoid(np.dot(X, self.weights1))
        self.output_layer = self.sigmoid(np.dot(self.hidden_layer, self.weights2))
        return self.output_layer

    def backward(self, X, y, output, learning_rate):
        # Retropropagación del error y ajuste de los pesos

        # Cálculo del error en la capa de salida
        output_error = y - output
        output_delta = output_error * self.sigmoid_derivative(output)

        # Cálculo del error en la capa oculta
        hidden_error = np.dot(output_delta, self.weights2.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_layer)

        # Ajuste de los pesos
        self.weights2 += np.dot(self.hidden_layer.T, output_delta) * learning_rate
        self.weights1 += np.dot(X.T, hidden_delta) * learning_rate

    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            # Propagación hacia adelante
            output = self.forward(X)

            # Retropropagación del error y ajuste de los pesos
            self.backward(X, y, output, learning_rate)

    def predict(self, X):
        # Realiza una predicción
        output = self.forward(X)
        return output.argmax(axis=1)


# Ejemplo de uso
# Supongamos que tenemos un conjunto de datos de entrada X y sus respectivas etiquetas y

# Definimos los parámetros de la red neuronal
input_size = 2
hidden_size = 3
output_size = 2

# Creamos una instancia de la red neuronal
nn = NeuralNetwork(input_size, hidden_size, output_size)

# Definimos los datos de entrenamiento
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0, 1], [1, 0], [1, 0], [0, 1]])

# Entrenamos la red neuronal
epochs = 1000
learning_rate = 0.1
nn.train(X, y, epochs, learning_rate)

# Realizamos una predicción con nuevos datos
new_data = np.array([[0, 1], [1, 0]])
predictions = nn.predict(new_data)

# Imprimimos las predicciones
for i in range(len(new_data)):
    print("Entrada:", new_data[i])
    print("Predicción:", predictions[i])
    print()
