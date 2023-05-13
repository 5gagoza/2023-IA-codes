"""Ingeniería del Conocimiento: Ontologías
    
    Busca representar el conocimiento de un dominio de modo que pueda ser entendido tanto por los seres humanos como por las máquinas

    Definir el dominio de la ontología.
    Determinar conceptos clave
    Definir las propiedades y relaciones de los conceptos.
    Establecer jerarquías y clasificaciones: Clases y subclases.
    Especificar reglas y restricciones.
    Utilizar un lenguaje formal: Utilizar un lenguaje formal, como RDF (Resource Description Framework) o OWL (Web Ontology Language), 
    para representar la ontología de manera precisa y legible para las máquinas.
    Validar la ontología.
    Aplicar la ontología.

"""

# Importar la biblioteca Owlready2 para trabajar con ontologías
from owlready2 import *

# Crear una ontología vacía
onto = Ontology("http://www.ejemplo.com/ontologia#")

# Definir una clase en la ontología
class Persona(Thing):
    # Agregar una etiqueta a la clase
    label = "Persona"

# Definir una propiedad en la ontología
class tieneEdad(Property):
    # Definir el dominio y rango de la propiedad
    domain = [Persona]
    range = [int]

# Crear instancias de la clase Persona
juan = Persona("Juan")
maria = Persona("Maria")

# Establecer valores de propiedades para las instancias
juan.tieneEdad = 30
maria.tieneEdad = 25

# Guardar la ontología en un archivo
onto.save("ontologia.owl")
