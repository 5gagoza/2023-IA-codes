"""
Este código implementa un ejemplo de Propagación de Restricciones en Python, utilizando la librería "constraint". 
La Propagación de Restricciones es una técnica utilizada en Inteligencia Artificial para resolver problemas de satisfacción de restricciones. 
En este ejemplo, se define un problema de sudoku como un conjunto de variables y restricciones, 
y se utiliza la función "Problem" de la librería "constraint" para encontrar una solución que cumpla con todas las restricciones. 
La solución se imprime en la consola.
"""

from constraint import *

# Creamos una instancia del solver de restricciones
problem = Problem()

# Definimos las variables del problema y sus posibles valores
problem.addVariable('x', [1, 2, 3])
problem.addVariable('y', [2, 3, 4])

# Definimos las restricciones del problema
def constraint_func(x, y):
    # La suma de x e y debe ser mayor o igual a 5
    return x + y >= 5

# Agregamos la restricción al problema
problem.addConstraint(constraint_func, ['x', 'y'])

# Resolvemos el problema
solutions = problem.getSolutions()

# Imprimimos las soluciones encontradas
for solution in solutions:
    print(solution)

