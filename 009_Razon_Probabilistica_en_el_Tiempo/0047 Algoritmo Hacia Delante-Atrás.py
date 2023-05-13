#Supongamos que tenemos un modelo oculto de Markov (Hidden Markov Model, HMM) con dos estados ocultos: "soleado" (S) y "lluvioso" (L). Queremos estimar la secuencia de estados ocultos dado una secuencia de observaciones (por ejemplo, la presencia de sombrillas en un día determinado).

import numpy as np

# Definir el modelo oculto de Markov (HMM)
estados_ocultos = ['S', 'L']
observaciones = ['No sombrilla', 'Sombrilla']

# Definir las probabilidades iniciales de los estados ocultos
pi = np.array([0.6, 0.4])

# Definir la matriz de transición de los estados ocultos
transiciones = np.array([[0.7, 0.3],
                         [0.4, 0.6]])

# Definir la matriz de emisión de las observaciones dada cada estado oculto
emisiones = np.array([[0.9, 0.1],
                      [0.2, 0.8]])

# Definir las observaciones
observaciones_secuencia = ['No sombrilla', 'Sombrilla', 'No sombrilla']

# Hacia Delante
alpha = np.zeros((len(observaciones_secuencia), len(estados_ocultos)))

for t, observacion in enumerate(observaciones_secuencia):
    for s, estado in enumerate(estados_ocultos):
        if t == 0:
            alpha[t, s] = pi[s] * emisiones[s, observaciones.index(observacion)]
        else:
            suma = np.sum(alpha[t-1] * transiciones[:, s])
            alpha[t, s] = suma * emisiones[s, observaciones.index(observacion)]

# Atrás
beta = np.ones((len(observaciones_secuencia), len(estados_ocultos)))

for t in range(len(observaciones_secuencia)-2, -1, -1):
    for s, estado in enumerate(estados_ocultos):
        suma = np.sum(beta[t+1] * transiciones[s, :] * emisiones[:, observaciones.index(observaciones_secuencia[t+1])])
        beta[t, s] = suma

# Calcular la probabilidad de la secuencia de observaciones
probabilidad = np.sum(alpha[-1])

# Calcular las probabilidades de los estados ocultos en cada paso de tiempo
probabilidades_estados = alpha * beta / probabilidad

# Imprimir los resultados
print("Probabilidad de la secuencia de observaciones:", probabilidad)
print("Probabilidades de los estados ocultos en cada paso de tiempo:")
for t, observacion in enumerate(observaciones_secuencia):
    print("P({}={}) = {:.4f}".format(observacion, estados_ocultos[0], probabilidades_estados[t, 0]))
    print("P({}={}) = {:.4f}".format(observacion, estados_ocultos[1], probabilidades_estados[t, 1]))
