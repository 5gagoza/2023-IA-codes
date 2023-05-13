#Supongamos que tenemos un modelo oculto de Markov para modelar el estado del clima en tres posibles estados: soleado, nublado y lluvioso. Queremos realizar inferencia sobre el estado del clima dadas una secuencia de observaciones (por ejemplo, la temperatura diaria).

import numpy as np

# Definir los estados ocultos y las observaciones
estados_ocultos = ['Soleado', 'Nublado', 'Lluvioso']
observaciones = ['Caliente', 'Templado', 'Frio']

# Definir las probabilidades iniciales de los estados ocultos
pi = np.array([0.4, 0.3, 0.3])

# Definir la matriz de transición de los estados ocultos
transiciones = np.array([[0.6, 0.3, 0.1],
                         [0.4, 0.4, 0.2],
                         [0.2, 0.5, 0.3]])

# Definir la matriz de emisión de las observaciones dada cada estado oculto
emisiones = np.array([[0.3, 0.4, 0.3],
                      [0.4, 0.4, 0.2],
                      [0.6, 0.3, 0.1]])

# Definir la secuencia de observaciones
secuencia_observaciones = ['Caliente', 'Templado', 'Frio']

# Inicializar el algoritmo de Viterbi
T = len(secuencia_observaciones)
N = len(estados_ocultos)
viterbi = np.zeros((T, N))
backpointer = np.zeros((T, N), dtype=int)

# Paso de inicialización
viterbi[0] = pi * emisiones[:, observaciones.index(secuencia_observaciones[0])]

# Paso de recursión
for t in range(1, T):
    for s in range(N):
        prob_transicion = viterbi[t-1] * transiciones[:, s]
        viterbi[t, s] = np.max(prob_transicion) * emisiones[s, observaciones.index(secuencia_observaciones[t])]
        backpointer[t, s] = np.argmax(prob_transicion)

# Paso de terminación
prob_max = np.max(viterbi[-1])
estado_final = np.argmax(viterbi[-1])

# Reconstruir la secuencia de estados ocultos
secuencia_estados_ocultos = [estados_ocultos[estado_final]]
for t in range(T-1, 0, -1):
    estado_final = backpointer[t, estado_final]
    secuencia_estados_ocultos.insert(0, estados_ocultos[estado_final])

# Imprimir los resultados
print("Secuencia de observaciones:", secuencia_observaciones)
print("Secuencia de estados ocultos más probable:", secuencia_estados_ocultos)
print("Probabilidad más probable:", prob_max)
