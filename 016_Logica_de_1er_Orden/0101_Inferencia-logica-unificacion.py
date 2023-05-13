"""Inferencia Lógica: Unificación

    Busca asignar valores a las variables para que una expresión sea verdadera

    Se checa si los valores a igualar son identicos, en caso de que no, prosigue
    Se verifica si alguno de los términos es una variable
    Se igualan los elementos de manera recursiva
    Se evaluan las asignaciones
    Se entrega el resultado

"""
# Función de unificación
def unificar(t1, t2, asignacion):
    if asignacion is None:
        return None

    if t1 == t2:  # Si los términos son iguales, no se requiere unificar
        return asignacion

    if es_variable(t1):  # Si t1 es una variable
        return unificar_variable(t1, t2, asignacion)

    if es_variable(t2):  # Si t2 es una variable
        return unificar_variable(t2, t1, asignacion)

    if es_compuesto(t1) and es_compuesto(t2):  # Si ambos términos son compuestos
        return unificar_argumentos(t1, t2, asignacion)

    return None  # Si ninguno de los casos anteriores se cumple, la unificación no es posible


def es_variable(termino):
    return isinstance(termino, str) and termino.islower()  # Una variable es una cadena en minúsculas


def unificar_variable(variable, termino, asignacion):
    if variable in asignacion:  # Si la variable ya tiene una asignación previa
        return unificar(asignacion[variable], termino, asignacion)

    asignacion_actualizada = asignacion.copy()  # Se crea una copia de la asignación actual
    asignacion_actualizada[variable] = termino  # Se asigna el valor del término a la variable
    return asignacion_actualizada


def es_compuesto(termino):
    return isinstance(termino, list)  # Un término compuesto es una lista


def unificar_argumentos(t1, t2, asignacion):
    if len(t1) != len(t2):  # Si los términos compuestos tienen diferente longitud, no se pueden unificar
        return None

    unificacion_actualizada = asignacion
    for arg1, arg2 in zip(t1, t2):  # Se itera sobre los argumentos de ambos términos compuestos
        unificacion_actualizada = unificar(arg1, arg2, unificacion_actualizada)
        if unificacion_actualizada is None:
            return None

    return unificacion_actualizada


# Ejemplo de uso
asignacion_inicial = {}  # Asignación inicial vacía
termino1 = ['padre', 'Juan', 'Carlos']
termino2 = ['padre', 'Juan', 'x']

resultado = unificar(termino1, termino2, asignacion_inicial)
print(resultado)

