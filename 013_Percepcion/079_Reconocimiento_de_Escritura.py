"""
El reconocimiento de escritura es la capacidad de un sistema de percepción 
para interpretar y convertir la escritura manuscrita en texto digital.
Involucra técnicas de procesamiento de imágenes, análisis de patrones y aprendizaje automático.
Se utiliza en aplicaciones como la digitalización de documentos, 
la autenticación de firmas y la transcripción automática de escritura a mano
"""
import tensorflow as tf
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.utils import to_categorical

# Cargar el dataset MNIST de dígitos escritos a mano
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Preprocesamiento de los datos
X_train = X_train / 255.0
X_test = X_test / 255.0
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Construir el modelo de reconocimiento de escritura a mano
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compilar y entrenar el modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_test, y_test))

# Evaluar el modelo con el conjunto de pruebas
_, accuracy = model.evaluate(X_test, y_test)
print('Accuracy: %.2f' % (accuracy * 100))
