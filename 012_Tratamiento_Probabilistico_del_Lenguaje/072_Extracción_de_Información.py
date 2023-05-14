"""
La extracción de información consiste en identificar y capturar 
información específica y estructurada (como nombres de personas, 
ubicaciones o fechas) a partir de textos no estructurados.
Se utilizan técnicas probabilísticas para identificar patrones y
relaciones entre entidades en el texto y extraer la información relevante.
"""

import re #Trabajar con expresiones regulares

def extract_information(text):
    # Expresiones regulares para buscar patrones de información
    name_pattern = r"Name: ([A-Za-z ]+)"
    age_pattern = r"Age: (\d+)"
    email_pattern = r"Email: (\w+@\w+\.\w+)"

    # Extracción de información utilizando las expresiones regulares
    # re.search para busqueda de coincidencias en el texto proporcionado
    name_match = re.search(name_pattern, text)
    age_match = re.search(age_pattern, text)
    email_match = re.search(email_pattern, text)

    # Obtención de los valores encontrados
    name = name_match.group(1) if name_match else None
    age = int(age_match.group(1)) if age_match else None
    email = email_match.group(1) if email_match else None

    # Retorno de los resultados como un diccionario
    return {"Name": name, "Age": age, "Email": email}

# Ejemplo de uso
text = "Name: John Doe\nAge: 30\nEmail: john.doe@example.com"
result = extract_information(text)
print(result)
