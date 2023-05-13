"""Eventos y Objetos Mentales: Creencias
    
    Buscan Representar y utilizar creencias como objetos mentales en un sistema de inteligencia artificial. 

    Definir creencias: Información que el sistema considera real.
    Representar las creencias en una base de datos.
    Actualizar creencias: Modificar o agregar.
    Gestionar posibles conflictos entre las creencias.
    
""" 

# Definición de una creencia
creencia = {
    "id": 1,                       # Identificador de la creencia
    "descripcion": "Llueve",       # Descripción de la creencia
    "valor_verdad": True            # Valor de verdad de la creencia (verdadera)
}

# Adquisición de creencias
# En este ejemplo, ingresaremos una creencia manualmente
# pero podrías obtenerla de una fuente externa como un sensor o una base de conocimiento
print("Ingrese una creencia:")
descripcion = input("Descripción: ")
valor_verdad = input("Valor de verdad (True/False): ")
nueva_creencia = {
    "id": 2,
    "descripcion": descripcion,
    "valor_verdad": bool(valor_verdad)
}

# Actualización de creencias
# Agregamos la nueva creencia a la lista de creencias existentes
creencias = [creencia, nueva_creencia]

# Razonamiento con creencias
# En este ejemplo, verificaremos si alguna creencia es verdadera
# y realizaremos una acción en función de ello
for creencia in creencias:
    if creencia["valor_verdad"]:
        print("La creencia '{}' es verdadera.".format(creencia["descripcion"]))
        # Aquí puedes agregar el código para realizar una acción en función de la creencia

# Gestión de conflictos
# En este ejemplo, no hay conflictos entre las creencias
# pero podrías implementar lógica adicional para resolver conflictos en caso de que ocurran

# Utilización de creencias en el comportamiento
# Las creencias pueden influir en la planificación de acciones y en la toma de decisiones
# Puedes agregar lógica adicional aquí para utilizar las creencias en el comportamiento del sistema
