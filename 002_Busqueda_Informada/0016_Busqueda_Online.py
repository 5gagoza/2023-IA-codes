import requests
import json

# Clave de API y ID de búsqueda personalizada
API_KEY = "tu_clave_de_API"
SEARCH_ENGINE_ID = "tu_ID_de_busqueda_personalizada"

# Realizar una solicitud HTTP a la API de Google Custom Search
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={''}&num=100"
response = requests.get(url)

# Verificar que la respuesta sea correcta
if response.status_code == 200:
    # Analizar la respuesta JSON
    data = json.loads(response.text)

    # Verificar si la clave "items" está en el diccionario
    if "items" in data:
        # Mostrar los títulos de los resultados de búsqueda
        for idx, item in enumerate(data["items"]):
            print(f"{idx + 1}. {item['title']}")
    else:
        print("No se encontraron resultados de búsqueda.")
else:
    print(f"Error al realizar la solicitud: {response.status_code}")
