

"""Encadenamiento hacia adelante y hacia atrás

    Su objetivo es tomar decisiones en base a la información disponible.

    Encadenamiento hacia adelante:
    Se analizan los hechos conocidos y se buscan las reglas que se cumplen con la información.
    Se aplican las reglas para sacar nuevas conclusiones.
    Se actualiza la lista de reglas.


    Encadenamiento hacia atrás:
    Se inicia con un objetivo a alcanzar.
    Se buscan reglas que nos lleven a ese objetivo.
    Se agregan las reglas que se cumplan.
    Se repite hasta llegar al objetivo o no poder más.

"""

# Base de reglas
reglas = [
    {"antecedentes": ["p"], "conclusion": "q"},
    {"antecedentes": ["q"], "conclusion": "r"},
    {"antecedentes": ["r"], "conclusion": "s"},
]

# Hechos iniciales
hechos_conocidos = ["p"]

# Encadenamiento hacia adelante
nuevas_conclusiones = []            #Lista de nuevas conclusiones
while True:
    aplicadas = False
    for regla in reglas:        # Se verifica si los antecedentes se conocen y si la conclusión no se conoce.
        if all(antecedente in hechos_conocidos for antecedente in regla["antecedentes"]) and regla["conclusion"] not in hechos_conocidos:
            hechos_conocidos.append(regla["conclusion"])        # Se actualiza la info conocida
            nuevas_conclusiones.append(regla["conclusion"])     # Se actualizan las conclusiones
            aplicadas = True
    if not aplicadas:
        break

# Imprimir las conclusiones obtenidas
print("Conclusión(es) obtenida(s):")
for conclusion in nuevas_conclusiones:
    print(conclusion)


# Base de reglas
reglas = [
    {"antecedentes": ["p"], "conclusion": "q"},
    {"antecedentes": ["q"], "conclusion": "r"},
    {"antecedentes": ["r"], "conclusion": "s"},
]

# Objetivo deseado
objetivo = "s"

# Encadenamiento hacia atrás
def encadenamiento_atras(objetivo, reglas, hechos_conocidos):
    if objetivo in hechos_conocidos:        # Se analiza si se conoce la información
        return True
    for regla in reglas:            
        if regla["conclusion"] == objetivo:
            cumplidas = True
            for antecedente in regla["antecedentes"]:       # Se checa si se conoce el antecedente
                if not encadenamiento_atras(antecedente, reglas, hechos_conocidos):     # Se utiliza una función recursiva para ver si se puede llegar al antecedente.
                    cumplidas = False       # Si no, no se puede aplicar
                    break
            if cumplidas:       # Si se cumple la regla     
                hechos_conocidos.append(regla["conclusion"])      #Se actualiza la lista 
                return True
    return False

# Realizar el encadenamiento hacia atrás
nuevas_conclusiones = []
encadenamiento_atras(objetivo, reglas, nuevas_conclusiones)

# Imprimir las conclusiones obtenidas
print("Conclusión(es) obtenida(s):")
for conclusion in nuevas_conclusiones:
    print(conclusion)
