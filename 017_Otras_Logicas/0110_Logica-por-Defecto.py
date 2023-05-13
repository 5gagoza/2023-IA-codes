"""Lógica Por Defecto
    
    Asume que la información inicial es real hasta que se pruebe lo contrario.

    Definir el conjunto de creencias iniciales.
    Definir reglas de inferencia.
    Inferencias por defecto: Si la regla se cumple con los hechos actuales se añade.
    Actualizar las creencias iniciales.
    Repetir
    Evaluar que no haya contradicciones.
    
"""

# Definir un conjunto de creencias iniciales
creencias = {
    "A": True,
    "B": True,
    "C": True
}

# Definir reglas de inferencia
reglas = [
    {"antecedentes": ["A", "B"], "conclusion": "D"},
    {"antecedentes": ["B", "C"], "conclusion": "E"},
    {"antecedentes": ["D"], "conclusion": "F"}
]

# Función para realizar inferencias por defecto
def inferir(creencias, reglas):
    nuevas_creencias = creencias.copy()  # Crear una copia de las creencias existentes
    
    for regla in reglas:
        antecedentes_cumplidos = True
        for antecedente in regla["antecedentes"]:   # Iteración de antecedentes en la regla actual
            if antecedente not in nuevas_creencias or not nuevas_creencias[antecedente]:    
                antecedentes_cumplidos = False      # No se cumple con los antecedentes. Se descarta la regla.
                break
        
        if antecedentes_cumplidos and regla["conclusion"] not in nuevas_creencias:
            nuevas_creencias[regla["conclusion"]] = True  # Agregar la conclusión como un nuevo hecho
    
    return nuevas_creencias

# Aplicar inferencias por defecto y actualizar las creencias hasta que no haya cambios
while True:
    nuevas_creencias = inferir(creencias, reglas)
    
    if nuevas_creencias == creencias:
        break  # No hay cambios en las creencias, salir del bucle
    
    creencias = nuevas_creencias

# Imprimir las creencias resultantes
print("Creencias finales:")
for hecho, valor in creencias.items():
    print(hecho + ": " + str(valor))
