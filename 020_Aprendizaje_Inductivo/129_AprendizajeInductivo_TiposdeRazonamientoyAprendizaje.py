# -*- coding: utf-8 -*-
"""
Created on Fri May 12 21:08:44 2023

@author: carlo

Tipos de Razonamiento y Aprendizaje
"""

import math
import pandas as pd

def entropy(p):
    if p == 0 or p == 1:
        return 0
    else:
        return -p * math.log2(p) - (1 - p) * math.log2(1 - p)

def information_gain(df, feature, target):
    total_entropy = entropy(df[target].sum() / len(df[target]))
    values = df[feature].unique()
    weighted_entropy = 0
    for value in values:
        p = len(df[df[feature] == value][target]) / len(df[target])
        weighted_entropy += p * entropy(df[df[feature] == value][target].sum() / len(df[df[feature] == value][target]))
    return total_entropy - weighted_entropy

def id3(df, features, target):
    if len(df[target].unique()) == 1:
        return df[target].unique()[0]
    elif len(features) == 0:
        return df[target].value_counts().idxmax()
    else:
        best_feature = max(features, key=lambda f: information_gain(df, f, target))
        tree = {best_feature: {}}
        remaining_features = [f for f in features if f != best_feature]
        for value in df[best_feature].unique():
            subset = df[df[best_feature] == value]
            subtree = id3(subset, remaining_features, target)
            tree[best_feature][value] = subtree
        return tree

# Ejemplo de uso
data = {'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
        'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
        'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
        'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
        'Play': [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0]}
df = pd.DataFrame(data)

features = ['Outlook', 'Temperature', 'Humidity', 'Wind']
target = 'Play'
tree = id3(df, features, target)
print(tree)
