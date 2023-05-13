"""Lógica temporal
    
    Busca modelar el comportamiento de las cosas en base al tiempo.

    Definición del modelo temporal: Un modelo que describa cómo evoluciona sobre el tiempo.
    Proposición de fórmulas lógicas para las afirmaciones o propiedades.
    Definir las reglas de inferencia temporal.
    Validar las proposiciones y realizar inferencias lógicas.
    Interpretación del resultado para predecir eventos.
    
"""


from temporal_logic import TemporalLogicEngine

# Creamos una instancia del motor de lógica temporal
engine = TemporalLogicEngine()

# Definimos las proposiciones atómicas
proposiciones = {
    'p': False,
    'q': True,
    'r': False
}

# Definimos las reglas temporales
reglas = [
    'p -> X q',  # p implica que en el siguiente estado q es verdadero
    'q -> G r',  # q implica que siempre (en todos los estados) r es verdadero
    'F r'        # r eventualmente se vuelve verdadero
]

# Cargamos las proposiciones y reglas en el motor
engine.load_props(proposiciones)
engine.load_rules(reglas)

# Verificamos las propiedades temporales
resultado = engine.verify_properties()

# Interpretamos los resultados
for propiedad, valor in resultado.items():
    if valor:
        print(f"La propiedad '{propiedad}' se cumple en el sistema.")
    else:
        print(f"La propiedad '{propiedad}' no se cumple en el sistema.")
