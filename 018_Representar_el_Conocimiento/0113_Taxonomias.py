"""Taxonomías: Categorías y Objetos
    
    Las taxonomías se utilizan para organizar y clasificar objetos en categorías jerárquicas, lo que facilita la estructuración y 
    comprensión de la información.

    Definir las categorías principales para categorizar.
    Establecer una jerarquía
    Asignar objetos a la jerarquía
        Al tener muchos objetos, tener cuidado con la coherencia.


"""

# Definición de las categorías
categorias = {
    'Animales': ['Perro', 'Gato', 'Elefante'],
    'Frutas': ['Manzana', 'Banana', 'Naranja'],
    'Vehículos': ['Automóvil', 'Motocicleta', 'Bicicleta']
}

# Función para buscar la categoría de un objeto
def buscar_categoria(objeto):
    for categoria, objetos in categorias.items():
        if objeto in objetos:
            return categoria
    return None

# Ejemplo de asignación de objetos a categorías
objetos = ['Perro', 'Banana', 'Motocicleta', 'Libro']
for objeto in objetos:
    categoria = buscar_categoria(objeto)
    if categoria:
        print(f'El objeto "{objeto}" pertenece a la categoría "{categoria}"')
    else:
        print(f'No se encontró una categoría para el objeto "{objeto}"')


