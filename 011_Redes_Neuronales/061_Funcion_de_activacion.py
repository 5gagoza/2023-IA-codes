"""
Las funciones de activación se utilizan en las neuronas 
artificiales para introducir no linealidades en la red 
neuronal. Estas funciones determinan la salida de una neurona
en función de su entrada ponderada. Algunos ejemplos comunes de 
funciones de activación son la función sigmoide, la función ReLU
y la función tangente hiperbólica.

"""
""" Funciones de activacion en redes neuronales"""

import numpy as np

# Funciones de Activación

# Función de activación sigmoidal valores entre 0 y 1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Función de activación ReLU devuele el valor de entrada si x>0, si x<0 entrega 0
def relu(x):
    return np.maximum(0, x)

# Función de activación tangente hiperbólica valores entre -1 y 1
def tanh(x):
    return np.tanh(x)

# Función de activación softmax calcula la exponencial de los valores de entrada y los normaliza 
def softmax(x):
    exps = np.exp(x)
    return exps / np.sum(exps)

# Ejemplo de uso de las funciones de activación

# Datos de entrada
x = np.array([1, -2, 0.5])

# Aplicar la función de activación sigmoidal
output_sigmoid = sigmoid(x)
print("Salida (sigmoidal):", output_sigmoid)

# Aplicar la función de activación ReLU
output_relu = relu(x)
print("Salida (ReLU):", output_relu)

# Aplicar la función de activación tangente hiperbólica
output_tanh = tanh(x)
print("Salida (tanh):", output_tanh)

# Datos de entrada para la función softmax
x_softmax = np.array([2, 1, 0.5])
# Aplicar la función de activación softmax
output_softmax = softmax(x_softmax)
print("Salida (softmax):", output_softmax)
