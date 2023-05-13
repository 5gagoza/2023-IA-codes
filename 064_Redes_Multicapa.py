"""
Las redes multicapa, también conocidas como redes neuronales feedforward,
son redes neuronales compuestas por múltiples capas de neuronas, incluyendo 
una capa de entrada, una o varias capas ocultas y una capa de salida. 
Estas redes pueden aprender representaciones de alto nivel y resolver 
problemas más complejos al introducir capas intermedias entre la entrada y la salida.
"""

""" Red neuronal multicapa utilizando capas densas """
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Generar datos de ejemplo
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, random_state=42)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de red neuronal que pertime usar capas de manera secuencial
model = Sequential()

# Agregar capas ocultas
model.add(Dense(units=32, activation='relu', input_dim=X.shape[1]))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=32, activation='relu'))

# Agregar capa de salida
model.add(Dense(units=1, activation='sigmoid'))

# Compilar el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=1)

# Evaluar el modelo en el conjunto de prueba
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Loss: {loss:.4f}')
print(f'Accuracy: {accuracy:.4f}')
