# -*- coding: utf-8 -*-
"""
Created on Fri May 12 20:39:30 2023

@author: carlo

Modelo Probabilista Racional:
    
El modelo probabilista racional se basa en la teoría de la probabilidad para tomar 
decisiones en situaciones inciertas. Aquí tienes un ejemplo de código que utiliza un 
modelo probabilista para tomar una decisión:
    
"""

import random

class DecisionModel:
    def __init__(self, options):
        self.options = options

    def make_decision(self):
        probabilities = self.calculate_probabilities()
        decision = random.choices(self.options, probabilities)[0]
        return decision

    def calculate_probabilities(self):
        total_weight = sum(option.weight for option in self.options)
        probabilities = [option.weight / total_weight for option in self.options]
        return probabilities

class Option:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

# Crear el modelo de decisión
options = [
    Option("Opción 1", 0.4),
    Option("Opción 2", 0.3),
    Option("Opción 3", 0.2),
    Option("Opción 4", 0.1)
]
decision_model = DecisionModel(options)

# Tomar una decisión
decision = decision_model.make_decision()
print(decision)  # Salida: una de las opciones (por ejemplo, "Opción 1")
