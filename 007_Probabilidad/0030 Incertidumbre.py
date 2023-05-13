import numpy as np

# Datos de ejemplo
data = np.array([2, 4, 6, 8, 10])

# Cálculo de la media y desviación estándar
mean = np.mean(data)
std = np.std(data)

# Cálculo del intervalo de confianza al 95%
confidence = 0.95
n = len(data)
z = 1.96  # Valor crítico para un nivel de confianza del 95%
margin_error = z * std / np.sqrt(n)

# Cálculo del intervalo de confianza
lower_bound = mean - margin_error
upper_bound = mean + margin_error

print("Media:", mean)
print("Desviación estándar:", std)
print("Intervalo de confianza al", confidence * 100, "%:")
print("(", lower_bound, ",", upper_bound, ")")
