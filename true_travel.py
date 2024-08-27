# definicion de clases
class Cliente:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Vuelo:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino

class Hotel:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

class Reserva:
    def __init__(self, cliente, vuelo_ida, vuelo_regreso, hotel):
        self.cliente = cliente
        self.vuelo_ida = vuelo_ida
        self.vuelo_regreso = vuelo_regreso
        self.hotel = hotel

class PaqueteTuristico:
    def __init__(self, ciudad, vuelo_ida, vuelo_regreso, hotel):
        self.ciudad = ciudad
        self.vuelo_ida = vuelo_ida
        self.vuelo_regreso = vuelo_regreso
        self.hotel = hotel

# creacion de variables compartidas

clientes = []
vuelos = []
hoteles = []
reservas = []
paquetes_turisticos = []