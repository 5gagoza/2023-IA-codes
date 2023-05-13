"""
Este código implementa un modelo de Markov oculto (HMM) para realizar el etiquetado de secuencias de observaciones. En particular, se utiliza un modelo HMM 
de dos estados ocultos (llamados "Sano" y "Enfermo") para etiquetar secuencias de observaciones que corresponden a pacientes sanos y enfermos.

El modelo HMM se entrena utilizando la biblioteca hmmlearn y se ajusta a los datos de entrenamiento (observaciones de pacientes sanos y enfermos). 
Luego, se utilizan las probabilidades de transición del modelo entrenado y la matriz de emisión de probabilidades para predecir las etiquetas ocultas (enfermo o sano) 
de una nueva secuencia de observaciones.
"""

from hmmlearn import hmm
import numpy as np

# Datos de entrenamiento
obs = np.array([[0.5], [1.0], [-0.3], [-1.5], [0.0]])

# Definir el modelo
model = hmm.GaussianHMM(n_components=2, covariance_type="diag")

# Entrenar el modelo
model.fit(obs)

# Predecir la secuencia de estados ocultos más probable para una nueva secuencia de observaciones
obs_new = np.array([[0.8], [-0.7], [0.2]])
logprob, state_sequence = model.decode(obs_new)

print("Log-probabilidad de la secuencia:", logprob)
print("Secuencia de estados ocultos más probable:", state_sequence)
