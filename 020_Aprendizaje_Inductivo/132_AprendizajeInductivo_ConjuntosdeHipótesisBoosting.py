# -*- coding: utf-8 -*-
"""
Created on Fri May 12 21:14:10 2023

@author: carlo

Conjuntos de Hipótesis: Boosting
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

# Cargar el conjunto de datos de ejemplo (Cáncer de mama)
cancer = load_breast_cancer()
X = cancer.data
y = cancer.target

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un conjunto de hipótesis mediante el algoritmo de Boosting con árboles de decisión
boosting = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=50)
boosting.fit(X_train, y_train)

# Evaluar el rendimiento del conjunto de hipótesis en el conjunto de prueba
accuracy = boosting.score(X_test, y_test)
print("Exactitud del conjunto de hipótesis mediante Boosting:", accuracy)

