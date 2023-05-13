"""Sintaxis y Semántica: Cuantificadores:

    Buscan definir la cantidad de elementos que cumplen ciertas condiciones

    Se crea una proposición lógica para el cuantificador.
    Se elige entre cuantificador universal (∀) o existencial (∃).
    Se establece el rango de elementos sobre los que se aplicará el cuantificador.
    Se especifican las condiciones y restricciones
    En función de los elementos y las condiciones se checa la verdad o falsedad de la expresión lógica.


"""


# Definición del conjunto de números
numeros = [1, 2, 3, 4, 5]

# Ejemplo de cuantificador universal (∀)
todos_mayores_a_cero = all(num > 0 for num in numeros)          # Checa si todos los num son mayores a cero
print("Todos los números son mayores a cero:", todos_mayores_a_cero)

# Ejemplo de cuantificador existencial (∃)
hay_numero_par = any(num % 2 == 0 for num in numeros)       # Checa si alguno de los num es mayores a cero
print("Hay al menos un número par:", hay_numero_par)
