"""Acciones, Situaciones y Eventos: Marcos
    
    Los marcos son estructuras de datos utilizadas para representar conocimiento sobre situaciones, 
    eventos o acciones en un dominio específico. 

    Definir estructura del marco: Propiedades importantes
    Se generan instancias para representar situaciones o eventos.
    Se almacena la información
    Establecer conexiones entre los marcos
    Actualizar los marcos 

"""

class Marco:
    def __init__(self, nombre, atributos):
        self.nombre = nombre
        self.atributos = atributos

marco_comida = Marco("Comida", {"tipo": "str", "cantidad": "int"})
print(marco_comida.nombre)  # salida: Comida
print(marco_comida.atributos)  # salida: {'tipo': 'str', 'cantidad': 'int'}
