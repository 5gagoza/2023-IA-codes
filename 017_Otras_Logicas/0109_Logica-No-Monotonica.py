"""Lógica no monotónica
    
    Permite razonar y tomar decisiones en un entorno incierto o con información incompleta

    Definir conjunto de hechos, reglas y suposiciones
    Inferencia inicial: Para conseguir conclusiones iniciales
    Actualizar la información con las nuevas conclusiones.
        Podría ser evaluando las conclusiones, cambiando las reglas de inferencia, etc.
    Repetir.
    
"""

# Definición de los hechos iniciales
hechos = {"A": True, "B": False, "C": True}

# Definición de las reglas
reglas = [
    {"antecedentes": ["A"], "conclusion": "D"},
    {"antecedentes": ["B"], "conclusion": "E"},
    {"antecedentes": ["C", "D"], "conclusion": "F"}
]

# Función para realizar la inferencia lógica
def inferencia_logica(hechos, reglas):
    cambios = True
    while cambios:
        cambios = False
        for regla in reglas:        # Se aplican las reglas y se evalua si los antecedentes continuan siendo verdaderos
            antecedentes_verdaderos = all(hechos.get(antecedente) for antecedente in regla["antecedentes"])
            if antecedentes_verdaderos and hechos.get(regla["conclusion"]) is None:
                hechos[regla["conclusion"]] = True
                cambios = True          # Cuando no hay más cambios, sale del while.

# Llamada a la función de inferencia lógica
inferencia_logica(hechos, reglas)

# Imprimir los hechos resultantes
print(hechos)
