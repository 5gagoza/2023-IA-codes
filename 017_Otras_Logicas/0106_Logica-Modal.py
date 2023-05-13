"""Lógicas modal

    Tipo de lógica que permite analizar proposiciones que son verdaderas en 
    diferentes "mundos posibles" o estados de conocimiento.

    Definición de mundos posibles o configuración de proposiciones.
    Definir los operadores modales:"necesario" (□) y "posible" (◇) para relacionar los mundos posibles
    Definir reglas de inferencia. Para poder combinar y evaluar proposiciones en diferentes mundos.
    Razonamiento modal: Probar las proposiciones en diferentes mundos e inferir en base a las reglas.
    Analizar las conclusiones en el contexto del problema.

"""

# Importar la librería 'modal' de PyModal
from pymodal import modal_logic

# Definir los mundos posibles
mundos = {'mundo1', 'mundo2', 'mundo3'}

# Definir las proposiciones
proposiciones = {'p', 'q', 'r'}

# Definir las relaciones entre las proposiciones y los mundos
relaciones = {
    'mundo1': {'p'},
    'mundo2': {'q'},
    'mundo3': {'r'}
}

# Definir las reglas de inferencia
reglas = [
    ('□p', 'p'),  # Regla de necesidad: si p es necesario, entonces p es verdadero
    ('◇q', 'q'),  # Regla de posibilidad: si q es posible, entonces q es verdadero
    ('p', 'q')    # Regla de implicación: si p es verdadero, entonces q es verdadero
]

# Crear una instancia del sistema de lógica modal
sistema_modal = modal_logic.ModalLogic(mundos, proposiciones, relaciones, reglas)

# Realizar el razonamiento modal
resultado = sistema_modal.evaluate('□p -> ◇q')  # Evaluamos la fórmula modal □p -> ◇q

# Imprimir el resultado
print(f"El resultado de la evaluación es: {resultado}")

