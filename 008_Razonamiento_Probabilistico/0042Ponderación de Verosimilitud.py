#Supongamos que tenemos un conjunto de observaciones y queremos estimar la probabilidad de obtener una cara en el lanzamiento de una moneda cargada desconocida. Utilizaremos el método de ponderación de verosimilitud para realizar esta estimación.

import numpy as np

# Definir el conjunto de observaciones
observaciones = ['Cara', 'Cara', 'Cruz', 'Cara']

# Definir el conjunto de pesos para cada observación
pesos = [0.2, 0.3, 0.5, 0.4]

# Calcular la probabilidad ponderada de obtener una cara
probabilidad = np.sum(np.array(observaciones) == 'Cara' * np.array(pesos)) / np.sum(pesos)

print("La probabilidad ponderada de obtener una cara es:", probabilidad)
