# -*- coding: utf-8 -*-
"""
Created on Fri May 12 20:36:49 2023

@author: carlo

Incertidumbre y Factores de Certeza:
    
Cuando se trata de incertidumbre, es común utilizar la teoría de probabilidades 
para manejarla. Aquí tienes un ejemplo de código que utiliza factores de certeza 
(certainty factors) para representar incertidumbre:
"""

class Fact:
    def __init__(self, name, certainty_factor):
        self.name = name
        self.certainty_factor = certainty_factor

# Crear los hechos con factores de certeza
fact1 = Fact("Llueve", 0.8)
fact2 = Fact("Hace frío", 0.6)

# Imprimir los hechos
print(fact1.name, fact1.certainty_factor)  # Salida: Llueve 0.8
print(fact2.name, fact2.certainty_factor)  # Salida: Hace frío 0.6
