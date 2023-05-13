#Supongamos que queremos generar y analizar un proceso estacionario en el dominio del tiempo. Utilizaremos un proceso AR(1) como ejemplo.

import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros del proceso AR(1)
phi = 0.5  # Coeficiente de autoregresión
mu = 0  # Media del proceso
sigma = 1  # Desviación estándar del ruido

# Definir la longitud de la secuencia temporal
n = 1000

# Generar el proceso AR(1)
x = np.zeros(n)
x[0] = np.random.normal(mu, sigma)
for i in range(1, n):
    x[i] = phi * x[i-1] + np.random.normal(mu, sigma)

# Graficar la secuencia temporal
plt.plot(x)
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Proceso AR(1)')
plt.show()

# Calcular la media y la autocovarianza del proceso
media = np.mean(x)
autocovarianza = np.correlate(x - media, x - media, mode='full') / n

# Graficar la autocovarianza
lags = np.arange(-n+1, n)
plt.stem(lags, autocovarianza)
plt.xlabel('Desfase')
plt.ylabel('Autocovarianza')
plt.title('Autocovarianza del Proceso AR(1)')
plt.show()
