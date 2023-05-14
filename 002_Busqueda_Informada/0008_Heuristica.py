def ordenar_lista(lista):
    # Heurística 1: Ordenar alfabéticamente si los elementos son cadenas de texto
    if all(isinstance(elem, str) for elem in lista):
        return sorted(lista)
    
    # Heurística 2: Ordenar de forma ascendente si los elementos son números
    if all(isinstance(elem, (int, float)) for elem in lista):
        return sorted(lista)
    
    # Heurística 3: Ordenar en función de la longitud de los elementos si son cadenas de texto
    if all(isinstance(elem, str) for elem in lista):
        return sorted(lista, key=len)
    
    # Heurística 4: Ordenar en función de la magnitud de los números si son números
    if all(isinstance(elem, (int, float)) for elem in lista):
        return sorted(lista, key=abs)
    
    # Si ninguna de las heurísticas anteriores se aplica, simplemente ordenar alfabéticamente
    return sorted(lista)

nombres = ["Juan", "Ana", "Luis", "Pedro", "Sofía", "María", "Beto"]

nombres_ordenados = ordenar_lista(nombres)

print(nombres_ordenados)