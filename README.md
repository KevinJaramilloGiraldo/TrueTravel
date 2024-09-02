# TrueTravel

TrueTravel es un sistema de gestión de clientes, hoteles, vuelos, paquetes turísticos y reservas para una agencia de viajes. Este proyecto está desarrollado en Python y permite gestionar eficientemente todas las operaciones relacionadas con los viajes y servicios turísticos ofrecidos por la agencia.

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## Características

- **Gestión de Clientes**: Permite agregar, buscar y gestionar información de clientes.
- **Gestión de Hoteles**: Permite gestionar hoteles, incluyendo la adición de nuevos hoteles y la búsqueda por nombre o ID.
- **Gestión de Vuelos**: Administra los vuelos, permitiendo agregar nuevos vuelos y buscar vuelos específicos.
- **Gestión de Paquetes Turísticos**: Gestiona paquetes turísticos que combinan vuelos y hoteles, permitiendo búsquedas y reservas.
- **Gestión de Reservas**: Facilita la creación y administración de reservas para los clientes.

## Requisitos

- Python 3.8 o superior

## Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/Leonard-Hernandez/TrueTravel
    cd TrueTravel
    ```

## Uso

1. **Ejecutar el sistema:**

    Para iniciar el sistema, ejecuta el archivo `main.py`:

    ```bash
    python main.py
    ```

2. **Navegar por el sistema:**

    El sistema cuenta con un menú principal que te permitirá navegar por las diferentes funcionalidades:
    
    - Clientes
    - Hoteles
    - Vuelos
    - Paquetes Turísticos
    - Reservas

3. **Limpiar la consola:**

    Cada vez que accedes a un menú, la consola se limpiará automáticamente para mejorar la experiencia de usuario. Además, el sistema mostrará un banner de bienvenida al inicio de cada sesión.

## Estructura del Proyecto

El proyecto está organizado en los siguientes directorios:

```plaintext
TrueTravel/
│
├───model/                  # Modelos de datos para el sistema (Clientes, Hoteles, etc.)
│
├───service/                # Lógica de negocio y servicios (gestión de Clientes, Hoteles, etc.)
│
├───utils/                  # Utilidades generales (como la función para mostrar el banner)
│
└───view/                   # Interfaz de usuario en consola (menús)