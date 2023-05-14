# -*- coding: utf-8 -*-
"""
Created on Fri May 12 21:15:54 2023

@author: carlo

 Árboles de Regresión M5
"""
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Cargar el conjunto de datos de Boston Housing
boston = load_boston()
X = boston.data
y = boston.target

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de Árbol de Regresión M5
model = DecisionTreeRegressor()
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular el error cuadrático medio (MSE)
mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)
