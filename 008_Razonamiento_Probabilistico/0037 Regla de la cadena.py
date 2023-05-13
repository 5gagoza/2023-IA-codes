#Supongamos que queremos calcular la probabilidad conjunta de dos variables, A y B, y tenemos la probabilidad condicional P(B|A) y la probabilidad marginal P(A). Podemos utilizar la Regla de la Cadena para obtener la probabilidad conjunta.

# Definir la probabilidad condicional P(B|A)
p_b_given_a = 0.7

# Definir la probabilidad marginal P(A)
p_a = 0.5

# Calcular la probabilidad conjunta P(A, B) utilizando la Regla de la Cadena
p_a_and_b = p_b_given_a * p_a

print("La probabilidad conjunta P(A, B) es:", p_a_and_b)
