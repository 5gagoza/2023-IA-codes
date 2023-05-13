"""
El código implementa un clasificador de máquinas de vectores soporte (SVM) con un kernel de función de base radial (RBF) para predecir la clasificación de una muestra de datos. 
El conjunto de datos se carga desde un archivo de texto y se divide en datos de entrenamiento y de prueba. Luego se crea un clasificador SVM con kernel RBF, 
se entrena con los datos de entrenamiento y se evalúa su rendimiento en los datos de prueba. 
Finalmente, se muestran las predicciones de clasificación para algunas muestras de prueba en la consola.
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Cargar conjunto de datos
iris = datasets.load_iris()

# Separar en características y etiquetas
X = iris.data
y = iris.target

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear un clasificador SVM
svm_clf = SVC(kernel='linear')

# Entrenar el clasificador con los datos de entrenamiento
svm_clf.fit(X_train, y_train)

# Hacer predicciones con los datos de prueba
y_pred = svm_clf.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)

# Imprimir la precisión del modelo
print("Precisión del modelo SVM:", accuracy)
