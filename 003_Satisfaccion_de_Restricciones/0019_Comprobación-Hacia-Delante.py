from typing import List, Tuple, Dict

def forward_checking(csp: Dict[str, Tuple[List[str], List[List[str]]]]):
    """Aplica el algoritmo de comprobación hacia delante a un problema de restricción
    (csp) representado como un diccionario que contiene las variables y sus dominios
    iniciales, así como las restricciones entre ellas.

    Args:
        csp (Dict[str, Tuple[List[str], List[List[str]]]]): El problema de restricción
        a resolver, donde las llaves son los nombres de las variables y los valores son
        tuplas que contienen una lista de los posibles valores de la variable y una lista
        de restricciones que deben cumplirse entre la variable y otras variables.

    Returns:
        Dict[str, str]: Un diccionario que asigna un valor a cada variable que satisface
        todas las restricciones, o None si no se encontró solución.
    """

    # Creamos un diccionario para almacenar las asignaciones de variables
    # y sus valores correspondientes
    assignment = {}

    # Inicializamos los conjuntos de variables no asignadas y las restricciones
    # no satisfechas
    unassigned_vars = set(csp.keys())
    constraints = {var: set() for var in csp.keys()}
    for var, (domain, relations) in csp.items():
        for relation in relations:
            for related_var in relation:
                constraints[var].add(related_var)

    # Definimos una función auxiliar para verificar si se han asignado valores
    # a todas las variables
    def is_complete():
        return len(unassigned_vars) == 0

    # Definimos una función auxiliar para verificar si se viola alguna restricción
    # después de asignar un valor a una variable
    def is_consistent(var, value):
        for related_var in constraints[var]:
            if related_var in unassigned_vars:
                continue
            if value == assignment.get(related_var):
                return False
        return True

    # Definimos una función auxiliar para actualizar los dominios de las variables
    # no asignadas después de asignar un valor a una variable
    def update_domains(var, value):
        for related_var in constraints[var]:
            if related_var in unassigned_vars:
                domain, relations = csp[related_var]
                for related_value in domain[:]:
                    assignment[related_var] = related_value
                    if not is_consistent(related_var, related_value):
                        domain.remove(related_value)
                    assignment.pop(related_var, None)
                if not domain:
                    return False
        return True

    # Definimos una función auxiliar para buscar el valor de la variable
    # con el dominio más pequeño
    def get_min_var():
        min_var = None
        min_size = float('inf')
        for var in unassigned_vars:
            size = len(csp[var][0])
            if size < min_size:
                min_var = var
                min_size = size
        return min_var

    # Definimos la función principal de búsqueda recursiva de soluciones
    def backtrack():
        if is_complete():
            return assignment

        var = get_min_var()
        domain = csp[var][0]
        for value in domain:
            if is_consistent(var, value):
                assignment[var] = value
                unassigned_vars.remove(var)
                if update_domains(var, value):
                    result = backtrack()
                    if result is not None:
                        return result
                assignment.pop(var, None)
                unassigned_vars.add(var)

        return None
    # Llamamos a la función de búsqueda recursiva de soluciones
    return backtrack()