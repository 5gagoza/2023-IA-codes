import numpy as np
from sklearn.naive_bayes import GaussianNB
import numpy as np

# Datos de ejemplo
X = np.array([[1, 2], [2, 1], [3, 4], [4, 3]])  # Características de los eventos
y = np.array([0, 0, 1, 1])  # Etiquetas de los eventos (0 o 1)

# Crear y entrenar el modelo de clasificación Naive Bayes
model = GaussianNB()
model.fit(X, y)

# Estimar la probabilidad a priori de la etiqueta 1
prior_probability = np.mean(y == 1)

print("Probabilidad a priori de la etiqueta 1:", prior_probability)
