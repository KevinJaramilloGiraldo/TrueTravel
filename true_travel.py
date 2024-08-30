# definicion de clases
class Cliente:
     # Variable de clase para el contador de IDs
    _id_counter = 1
    
    def __init__(self, nombre, apellido):
        self.id = Cliente._id_counter
        self.nombre = nombre
        self.apellido = apellido
        
        # Incrementar el contador de IDs para el siguiente cliente
        Cliente._id_counter += 1

class Vuelo:
    _id_counter = 1
    def __init__(self, origen, destino):
        self.id = Vuelo._id_counter
        self.origen = origen
        self.destino = destino

        Vuelo._id_counter += 1

class Hotel:
    _id_counter = 1
    def __init__(self, nombre, ciudad):
        self.id = Hotel._id_counter
        self.nombre = nombre
        self.ciudad = ciudad

        Hotel._id_counter += 1

class Reserva:
    _id_counter = 1
    def __init__(self, cliente, vuelo_ida, vuelo_regreso, hotel):
        self.id = Reserva._id_counter
        self.cliente = cliente
        self.vuelo_ida = vuelo_ida
        self.vuelo_regreso = vuelo_regreso
        self.hotel = hotel

        Reserva._id_counter += 1

class PaqueteTuristico:
    _id_counter = 1
    def __init__(self, ciudad, vuelo_ida, vuelo_regreso, hotel):
        self.ciudad = ciudad
        self.vuelo_ida = vuelo_ida
        self.vuelo_regreso = vuelo_regreso
        self.hotel = hotel

        PaqueteTuristico._id_counter += 1

# variables compartidas
clientes = [
    Cliente("Juan", "Perez"),
    Cliente("Maria", "Gonzalez"),
    Cliente("Pedro", "Lopez"),
    Cliente("Ana", "Martinez"),
]
vuelos = [
    Vuelo("Lima", "Cusco"),
    Vuelo("Cusco", "Lima"),
    Vuelo("bogota", "lima"),
    Vuelo("lima", "bogota"),
]
hoteles = [
    Hotel("Hilton", "Lima"),
    Hotel("Sheraton", "Cusco"),
    Hotel("Hotel Bolivar", "Bogota"),
    Hotel("Casa Blanca", "Lima"),
]
reservas = []
paquetes_turisticos = []

# Funciones

# Funciones de cliente

def agregarClientes (nombre, apellido):

    for i in clientes:
        if i.nombre==nombre and i.apellido==apellido:
                print ("El cliente ya existe")
                return
    newCliente=Cliente(nombre,apellido)
    clientes.append(newCliente)
    print ("Cliente creado con exito")
    
    return

# Funciones de paquetes turisticos

# Funciones de reservas

# Funciones de hoteles

# Funciones de vuelos

# Interfaz de usuario
