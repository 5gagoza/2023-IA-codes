#Supongamos que queremos generar muestras de una distribución exponencial con parámetro lambda utilizando el método de muestreo directo.
import numpy as np
#por directo 
# Definir el parámetro lambda de la distribución exponencial
lmbda = 0.5

# Generar una muestra de la distribución exponencial utilizando el método de muestreo directo
sample = np.random.exponential(scale=1/lmbda)

print("Muestra generada:", sample)

#por rechazo

import numpy as np
import matplotlib.pyplot as plt

# Definir la función de densidad de la distribución normal estándar
def normal_density(x):
    return np.exp(-x**2/2) / np.sqrt(2*np.pi)

# Definir la función de densidad de la distribución de prueba exponencial
def exponential_density(x, lmbda):
    return lmbda * np.exp(-lmbda * x)

# Definir el rango de valores para generar las muestras
x = np.linspace(-4, 4, 1000)

# Generar muestras de la distribución normal estándar utilizando el método de muestreo por rechazo
samples = []
num_samples = 1000

while len(samples) < num_samples:
    x_sample = np.random.exponential(scale=1)
    y_sample = np.random.uniform(0, normal_density(x_sample))
    if y_sample < normal_density(x_sample):
        samples.append(x_sample)

# Graficar las distribuciones
plt.plot(x, normal_density(x), label='Distribución Normal Estándar')
plt.plot(x, exponential_density(x, 1), label='Distribución de Prueba Exponencial')
plt.hist(samples, bins=30, density=True, label='Muestras')
plt.xlabel('x')
plt.ylabel('Densidad')
plt.legend()
plt.show()
