import numpy as np

# Generar datos de ejemplo
np.random.seed(0)
A = np.random.randint(0, 2, size=100)  # Evento A (0 o 1)
B = np.random.randint(0, 2, size=100)  # Evento B (0 o 1)

# Calcular la probabilidad condicionada P(A|B)
p_A_given_B = np.mean(A[B == 1])

# Calcular la probabilidad condicionada P(A|¬B)
p_A_given_not_B = np.mean(A[B == 0])

# Normalizar las probabilidades
p_normalized = [p_A_given_B, p_A_given_not_B] / sum([p_A_given_B, p_A_given_not_B])

print("Probabilidad condicionada P(A|B):", p_A_given_B)
print("Probabilidad condicionada P(A|¬B):", p_A_given_not_B)
print("Probabilidades normalizadas:", p_normalized)
