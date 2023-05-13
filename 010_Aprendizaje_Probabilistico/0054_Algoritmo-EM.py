"""
Este código implementa el algoritmo Expectation-Maximization (EM), que es una técnica de optimización utilizada en el aprendizaje no supervisado de modelos probabilísticos, 
en particular, en modelos de mezcla de gaussianas.

En resumen, el algoritmo EM alterna entre dos pasos: el paso de Expectación (E) y el paso de Maximización (M). En el paso E, se estima la probabilidad de 
pertenencia de cada punto a cada componente de la mezcla, mientras que en el paso M, se estiman los parámetros de cada componente de la mezcla a partir de las 
probabilidades estimadas en el paso E.

El proceso se repite hasta que se alcanza una convergencia satisfactoria, es decir, hasta que los valores de los parámetros convergen a un máximo local.
"""

from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

# Generamos un conjunto de datos sintéticos con tres grupos distintos
X, y_true = make_blobs(n_samples=300, centers=3, cluster_std=0.5, random_state=0)

# Ajustamos un modelo de mezcla de Gaussianas utilizando el algoritmo EM
gmm = GaussianMixture(n_components=3, covariance_type='full', max_iter=100)
gmm.fit(X)

# Predecimos las etiquetas para los puntos de datos utilizando el modelo ajustado
y_pred = gmm.predict(X)

# Mostramos los resultados en la consola
print('Etiquetas verdaderas:')
print(y_true)
print('Etiquetas predichas:')
print(y_pred)
