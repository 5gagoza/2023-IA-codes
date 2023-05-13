"""Lógicas de Orden Superior

    Son como extensiones que se le añaden a la lógica tradicional para poder realizar inferencias más sofisticadas.

    Creación de axiomas y reglas para guiar el razonamiento lógico.
    Definir funciones de alto nivel para representar el conocimiento. 
    Realizar las inferencias en base al conocimiento y reglas.
    Validación de inferencias.
    Iteración del proceso.

"""


from functools import reduce

# Predicados de orden superior
def es_figura_geometrica(figura):           # Determina si es alguna figura geométrica
    figuras_geometricas = ["cuadrado", "rectangulo", "circulo"]
    return figura in figuras_geometricas

def tiene_lados(figura, num_lados):            # Crea reglas en base a los lados de una figura
    num_lados_figura = {
        "cuadrado": 4,
        "rectangulo": 4,
        "circulo": 0
    }
    return figura in num_lados_figura and num_lados_figura[figura] == num_lados

# Funciones de orden superior
def calcular_area(figura):
    """Función que calcula el área de una figura geométrica."""
    areas_figuras = {
        "cuadrado": lambda a: a ** 2,
        "rectangulo": lambda a, b: a * b,
        "circulo": lambda r: 3.1415 * r ** 2
    }
    return areas_figuras[figura]

# Conocimiento representado
figuras = ["cuadrado", "rectangulo", "circulo"]

# Inferencias. Resultados filtrados en base a las caracs de la figura
figuras_geometricas = list(filter(es_figura_geometrica, figuras))
figuras_con_4_lados = list(filter(lambda figura: tiene_lados(figura, 4), figuras))
areas = list(map(calcular_area, figuras))

# Resultados
print("Figuras geométricas:", figuras_geometricas)
print("Figuras con 4 lados:", figuras_con_4_lados)
print("Áreas:", areas)
