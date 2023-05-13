"""Reglas de Diagnóstico y Causales:

    Busca las causas de una situación determinada en base a hechos e información conocida.

    Se recopilan reglas que estén relacionadas con las posibles causas
    También los eventos que podrían estar relacionados con la causa.
    Se comparan las reglas con los síntomas (eventos)
    Se generan conclusiones en base a las reglas que aplican.
    Si hay varias causas se determina una prioridad de causas.
    
"""
# Definición de reglas
reglas = [
    {"sintomas": ["fiebre", "tos"], "causa": "resfriado"},          # Conocimiento de las posibles causas
    {"sintomas": ["dolor de garganta"], "causa": "amigdalitis"},
    {"sintomas": ["fiebre", "dolor de cabeza"], "causa": "migraña"},
    {"sintomas": ["dolor de cabeza", "visión borrosa"], "causa": "migraña"}
]

# Síntomas observados
sintomas_observados = ["fiebre", "dolor de cabeza"]

# Búsqueda de causas
causas_probables = []
for regla in reglas:
    if all(sintoma in sintomas_observados for sintoma in regla["sintomas"]):
        causas_probables.append(regla["causa"])         # Actualizamos las causas probables

# Presentación del diagnóstico
if causas_probables:
    print("Las posibles causas del problema son:")
    for causa in causas_probables:
        print("- ", causa)
else:
    print("No se encontraron causas probables para los síntomas observados.")
