
"""Inferencia Lógica Proposicional

    Se utiliza para sacar deducciones lógicas en base a reglas o proposiciones.
    Se definen las proposiciones, luego se convierten a una forma lógica.
    En base a reglas de inferencia se deducen las conclusiones.
    Ese nuevo conocimiento se añade al conjunto de reglas.
    Repetir hasta que no se puedan sacar más conclusiones.


"""

# Definir los símbolos proposicionales
p = True
q = False

# Reglas y hechos iniciales
reglas = [
    (p and q, "p and q es verdadero"),      # Proposiciones escritas en forma lógica.
    (not p, "p es falso")
]

# Función de inferencia
def inferencia(reglas, simbolos):
    nuevas_conclusiones = []            # Lista de nuevas conclusiones.
    
    for regla, conclusion in reglas:
        if regla:
            nuevas_conclusiones.append(conclusion)      # Si se cumple la regla se añade a la lista.
    
    return nuevas_conclusiones

# Realizar la inferencia
conclusiones = inferencia(reglas, [p, q])           # Se actualiza la base de datos.

# Imprimir las conclusiones obtenidas
for conclusion in conclusiones:
    print(conclusion)
