# -*- coding: utf-8 -*-
"""
Created on Fri May 12 21:12:56 2023

@author: carlo
"""

import numpy as np
from collections import Counter

def entropy(y):
    counter = Counter(y)
    probs = [counter[c] / len(y) for c in set(y)]
    return -sum(p * np.log2(p) for p in probs)

def information_gain(X, y, feature):
    ent = entropy(y)
    vals, counts = np.unique(X[:, feature], return_counts=True)
    weighted_ent = sum((counts[i] / len(y)) * entropy(y[X[:, feature] == vals[i]]) for i in range(len(vals)))
    return ent - weighted_ent

def id3(X, y, features):
    if len(set(y)) == 1:
        return y[0]
    if len(features) == 0:
        return Counter(y).most_common(1)[0][0]
    best_feature = max(features, key=lambda f: information_gain(X, y, f))
    tree = {best_feature: {}}
    remaining_features = [f for f in features if f != best_feature]
    for val in np.unique(X[:, best_feature]):
        X_subset = X[X[:, best_feature] == val]
        y_subset = y[X[:, best_feature] == val]
        tree[best_feature][val] = id3(X_subset, y_subset, remaining_features)
    return tree

# Ejemplo de uso
X = np.array([[1, 'Soleado'], [1, 'Soleado'], [0, 'Nublado'], [0, 'Lluvioso'], [0, 'Lluvioso'], [1, 'Lluvioso'], [0, 'Nublado'], [1, 'Soleado'], [0, 'Soleado'], [0, 'Lluvioso'], [1, 'Soleado'], [0, 'Nublado'], [0, 'Nublado'], [1, 'Lluvioso']])
y = np.array(['No', 'No', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No'])
features = [0, 1]  # Índices de las características: 0 para 'Tiempo' y 1 para 'Outlook'
tree = id3(X, y, features)
print(tree)
