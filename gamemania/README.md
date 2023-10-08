# Proyecto GameManía.cl

- ***Ramo***: Programación Web
- ***Profesor***: Benjamín Mora <bej.mora@profesor.duoc.cl>

## Instalación
1. Instalar [``Python``](https://www.python.org/downloads/)
2. Instalar [``pip``](https://pip.pypa.io/en/stable/installation/)
3. Instalar [``Django``](https://www.djangoproject.com/download/)
4. Clonar este repositorio en una carpeta deseada
    ```bash
    git clone https://github.com/frcerdas/analista-programador.git
    ```
5. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
6. Precargar datos en base de datos
    ```bash
    python manage.py migrate loaddata precarga
    ```
7. Crear un superusuario para acceder a /admin
    ```bash
    python manage.py createsuperuser
    ```
8. Ejecutar servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```