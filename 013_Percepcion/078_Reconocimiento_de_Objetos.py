"""
El reconocimiento de objetos se refiere a la capacidad de un sistema
de percepción para identificar y clasificar objetos en una imagen o en un entorno.
Implica el uso de algoritmos y técnicas de aprendizaje automático para extraer 
características y patrones relevantes de las imágenes y compararlos con modelos predefinidos.
"""
import cv2

# Cargar el clasificador de Haar
cascade_path = 'haarcascade_hand.xml'
cascade = cv2.CascadeClassifier(cascade_path)

# Cargar la imagen
image_path = 'hands.jpg'
image = cv2.imread(image_path)

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar objetos utilizando el clasificador de Haar
objects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Dibujar un rectángulo alrededor de cada objeto detectado
for (x, y, w, h) in objects:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Mostrar la imagen con los objetos detectados
cv2.imshow('Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
