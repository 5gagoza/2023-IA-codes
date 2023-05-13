"""Programación Lógica: Prolog y CLIPS:

    Se utiliza para resolver problemas mediante la formulación de reglas lógicas y consultas que representan conocimiento y 
    relaciones entre entidades.

    Prolog:
        Define hechos y reglas.
        Busca soluciones que cumplan las condiciones.
        Unifica
        Utiliza backtracking

    CLIPS:
        Define hechos y reglas.
        Busca patrones y coincidencias.
        Dispara reglas que coincidan con los patrones.
        Cada regla activa acciones anidadas que podrían modificar los datos actuales.
        Se itera hasta que no se disparen más reglas o no se modifiquen más los datos.
    
"""

from pyke import knowledge_engine

# Definir las reglas del sistema
engine = knowledge_engine.engine(__file__)

# Definimos una regla:
# Por cada hecho datos.hecho con una variable x,
# se debe agregar un nuevo hecho datos.resultado con el mismo valor de x.
engine.add_rule("""
    foreach
        datos.hecho(x=<x>)
    assert
        datos.resultado(x=<x>)
""")

# Establecer los hechos iniciales

engine.assert_('datos.hecho', 'x', 5)
engine.assert_('datos.hecho', 'x', 10)
engine.assert_('datos.hecho', 'x', 15)

# Ejecutar el motor de reglas
engine.activate('datos')

# Obtener los resultados
results = list(engine.get('datos.resultado', 'x'))

# Imprimir los resultados obtenidos

for result in results:
    print(result['x'])


