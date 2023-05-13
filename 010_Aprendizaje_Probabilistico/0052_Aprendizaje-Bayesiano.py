"""
El código implementa un modelo de aprendizaje bayesiano utilizando la biblioteca PyMC3 en Python. En particular, se usa para estimar los parámetros de una 
distribución de probabilidad previa (normal) y actualizarla con datos observados mediante una distribución posterior.

El ejemplo utilizado en el código se refiere a la estimación de la media y la desviación estándar de una distribución normal a partir de un conjunto de datos observados. 
El modelo bayesiano asume que la media y la desviación estándar de la distribución priori son desconocidas, pero se pueden estimar a partir de los datos observados. 

El resultado final del código es una estimación de la distribución posterior de la media y la desviación estándar de la distribución normal, 
junto con información sobre la incertidumbre asociada a estas estimaciones. 
Este tipo de enfoque bayesiano es útil en situaciones donde los datos son limitados o inciertos y se requiere una evaluación cuidadosa de la 
incertidumbre en las estimaciones de los parámetros.
"""

from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargamos el conjunto de datos Iris
data = load_iris()

# Dividimos el conjunto de datos en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Creamos el clasificador de Naive Bayes
clf = GaussianNB()

# Entrenamos el clasificador con los datos de entrenamiento
clf.fit(X_train, y_train)

# Realizamos la predicción con los datos de prueba
y_pred = clf.predict(X_test)

# Medimos la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)

# Imprimimos la precisión obtenida
print("Precisión:", accuracy)
