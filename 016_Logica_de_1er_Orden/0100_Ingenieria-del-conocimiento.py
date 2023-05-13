
"""Ingenieria del conocimiento

    La Ingeniería del Conocimiento tiene como objetivo capturar, 
    representar y utilizar el conocimiento humano para resolver problemas mediante sistemas de inteligencia artificial.

    Adquirir conocimiento
    Representar conocimiento
    Desarrollar un sistema
    Se prueba y evalua
    Se actualiza conforme vaya necesitando

"""

# 1. Identificación del dominio: Sistema de recomendación de películas

# 2. Adquisición de conocimiento: Obtener preferencias de películas de los usuarios
usuarios = {
    "Juan": ["acción", "aventura", "suspenso"],
    "María": ["drama", "romance", "comedia"],
    "Pedro": ["acción", "comedia", "ciencia ficción"],
    # ... otros usuarios y sus preferencias
}

# 3. Representación del conocimiento: Crear reglas para recomendar películas
reglas = [
    (["acción", "aventura"], "Recomendar una película de superhéroes"),
    (["drama", "romance"], "Recomendar una película romántica"),
    (["comedia"], "Recomendar una película cómica"),
    # ... otras reglas de recomendación
]

# 4. Desarrollo del sistema: Implementar la lógica del sistema
def recomendar_pelicula(usuario):
    for regla in reglas:
        if all(preferencia in usuario for preferencia in regla[0]):
            return regla[1]
    return "No se pudo encontrar una recomendación"

# 5. Pruebas y evaluación: Probar el sistema de recomendación
usuario1 = usuarios["Juan"]
recomendacion1 = recomendar_pelicula(usuario1)
print("Recomendación para Juan:", recomendacion1)

usuario2 = usuarios["María"]
recomendacion2 = recomendar_pelicula(usuario2)
print("Recomendación para María:", recomendacion2)

# 6. Mantenimiento y actualización: Actualizar reglas y conocimiento según feedback de los usuarios, agregar nuevas películas, etc.
