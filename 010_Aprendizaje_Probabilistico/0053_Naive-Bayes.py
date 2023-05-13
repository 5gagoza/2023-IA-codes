"""
Este código implementa el algoritmo de clasificación Naïve-Bayes para predecir la clase de un conjunto de datos basándose en la probabilidad de ocurrencia de cada atributo 
y su relación con la clase objetivo. En este caso, se utiliza el modelo Naïve-Bayes Gaussiano, que asume que cada atributo sigue una distribución normal 
y que los atributos son independientes entre sí.

El código primero carga un conjunto de datos de entrenamiento y de prueba, y separa los atributos de las clases objetivo. 
Luego, se ajusta el modelo Naïve-Bayes Gaussiano a los datos de entrenamiento y se utiliza para predecir las clases del conjunto de prueba. 
Finalmente, se calcula la precisión de las predicciones y se imprime en la consola.
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Creamos el vectorizador y transformamos los textos de entrenamiento
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(["Este es un texto de ejemplo", "Otro texto de ejemplo", "Y otro más"])

# Definimos las etiquetas de cada texto de entrenamiento
y_train = ["categoria 1", "categoria 2", "categoria 2"]

# Creamos el clasificador Naive Bayes y lo entrenamos
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Clasificamos nuevos textos
X_new = vectorizer.transform(["Texto a clasificar"])
predicted = clf.predict(X_new)

# Imprimimos la categoría predicha
print(predicted)
