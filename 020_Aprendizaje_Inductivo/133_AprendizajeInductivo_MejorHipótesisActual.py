# -*- coding: utf-8 -*-
"""
Created on Fri May 12 21:22:16 2023

@author: carlo

Mejor Hipótesis Actual
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
model = LogisticRegression()
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Obtener la mejor hipótesis actual
best_hypothesis = model.coef_
print("Best Hypothesis:", best_hypothesis)


"""
En este ejemplo, se utiliza el conjunto de datos Iris, que contiene características y 
etiquetas de diferentes tipos de flores. Se divide el conjunto de datos en entrenamiento 
y prueba utilizando train_test_split de la librería scikit-learn.

A continuación, se crea un modelo de clasificación utilizando LogisticRegression de 
la misma librería. El modelo se entrena utilizando los datos de entrenamiento (X_train 
y y_train).

Después de entrenar el modelo, se realizan predicciones en el conjunto de prueba (X_test) 
utilizando el método predict. Finalmente, se calcula la precisión del modelo comparando las
 predicciones con las etiquetas reales utilizando accuracy_score de la librería scikit-learn
, y se imprime el resultado.
"""