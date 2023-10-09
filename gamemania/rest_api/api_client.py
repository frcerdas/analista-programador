import requests

# URL de la API
url = 'http://tu-dominio.com/api/lista_categorias/'

# Datos de la nueva categoría que deseas crear
nueva_categoria = {
    "nombreCategoria": "Nueva Categoría",
    "imagen": "ruta_de_la_imagen.jpg",
}

# Realiza una solicitud HTTP POST para crear la categoría
response = requests.post(url, data=nueva_categoria)

# Verifica la respuesta
if response.status_code == 201:
    print("Categoría creada exitosamente.")
    print(response.json())
else:
    print("Error al crear la categoría.")
    print(response.status_code)
    print(response.json())
