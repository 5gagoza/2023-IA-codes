"""
El aprendizaje profundo, también conocido como deep learning, 
es un subcampo del aprendizaje automático (machine learning) que 
se centra en el entrenamiento de modelos de redes neuronales 
artificiales profundas. Estas redes están compuestas por múltiples 
capas ocultas y son capaces de aprender representaciones jerárquicas de los datos

"""

"""El código muestra cómo entrenar una red neuronal 
para la clasificación de imágenes utilizando el conjunto de datos MNIST"""
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Cargar y dividir el conjunto de datos MNIST
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data() # Carga de conjunto de datos MNIST desde keras

# Normalizar las imágenes (convertirlas a 0 y 1) y convertir las etiquetas en categorías
x_train = x_train / 255.0
x_test = x_test / 255.0
y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

# Definir la arquitectura del modelo
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # Capa de entrada: aplanar las imágenes en un vector 1D
    keras.layers.Dense(128, activation='relu'),  # Capa oculta: 128 neuronas con función de activación ReLU
    keras.layers.Dropout(0.2),  # Capa de regularización: desactiva aleatoriamente el 20% de las neuronas para evitar el sobreajuste
    keras.layers.Dense(10, activation='softmax')  # Capa de salida: 10 neuronas con función de activación softmax para la clasificación multiclase
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(x_train, y_train, epochs=10, batch_size=32, verbose=1) # (epocas, tamaño de lote y verbosidad)

# Evaluar el modelo
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print('Precisión en el conjunto de prueba:', test_acc)

# Guardar el modelo entrenado
model.save('modelo_entrenado.h5') #formato de archivo binario que permite almacenar grandes 
                                    #cantidades de datos y metadatos de manera eficiente
