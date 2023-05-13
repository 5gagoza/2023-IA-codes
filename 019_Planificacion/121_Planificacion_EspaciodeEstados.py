# -*- coding: utf-8 -*-
"""
Created on Fri May 12 20:44:07 2023

@author: carlo

Espacio de Estados:
El espacio de estados es una representación formal del conjunto de todos los estados 
posibles de un sistema. Aquí tienes un ejemplo básico de código para representar un espacio 
de estados en Python:
"""

class Estado:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

# Definir el espacio de estados
espacio_estados = []

for x in range(5):
    for y in range(5):
        estado = Estado(x, y)
        espacio_estados.append(estado)

# Imprimir los estados
for estado in espacio_estados:
    print(estado)  # Salida: (0, 0), (0, 1), (0, 2), ..., (4, 3), (4, 4)

"""
En este ejemplo, el espacio de estados está representado por una lista de objetos de la 
clase "Estado". Cada objeto representa un estado con coordenadas (x, y), y se crea un 
objeto para cada combinación de valores posibles de x e y.
"""