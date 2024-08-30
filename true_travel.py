import os
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

def agregarHotel(nombre, ciudad):

    for hotel in hoteles:
        if hotel.nombre == nombre and hotel.ciudad == ciudad:
                print ("El hotel ya existe")
                return
            
    newHotel = Hotel(nombre,ciudad)
    hoteles.append(newHotel)
    print ("Hotel creado con éxito")
    
    return

# Funciones de vuelos

def agregarVuelo(origen, destino):
    
    for vuelo in vuelos:
        if vuelo.origen == origen and vuelo.destino == destino:
            print("El vuelo ya existe")
            return
    
    newVuelo = Vuelo(origen, destino)
    vuelos.append(newVuelo)
    print("Vuelo creado con éxito")
    
    return

# Interfaz de usuario

# Interfaces de Cliente
def interfazCrearCliente():

    # limpiando consola
    os.system("cls")

    # Crear cliente
    print("CREAR CLIENTE (presione x para volver al menu)")

    print("Ingresa el nombre: ")
    nombre = input()
    # Validar que el usuario no quiera volver al menu
    if nombre == "x":
        return
    
    print("Ingresa el apellido: ")
    apellido = input()
    # Validar que el usuario no quiera volver al menu
    if apellido == "x":
        return
    
    # Crear cliente
    agregarClientes(nombre, apellido)
    input("Presione enter para volver al menu")

def interfazListarClientes():
    #limpiando consola
    os.system("cls")

    # Metodos de consulta
    print("Como deseas Consultar?")
    print("1. Por ID")
    print("2. Por Nombre y apellido")
    print("3. Listar todos los clientes")
    comand = input()

    #por id
    if comand == "1":

        print("no implementado todavia")

    #por nombre y apellido
    elif comand == "2":

        print("no implementado todavia")

    #listar todos los clientes
    elif comand == "3":

        print("Listado de clientes")

        for i in clientes:
            print(f"{i.id} {i.nombre} {i.apellido}")

        input("Presione enter para volver al menu")

comand = ""
while True:
    #banner
    print(
        """
             ███████████                                   █████                                             ████ 
            ░█░░░███░░░█                                  ░░███                                             ░░███ 
            ░   ░███  ░  ████████  █████ ████  ██████     ███████   ████████   ██████   █████ █████  ██████  ░███ 
                ░███    ░░███░░███░░███ ░███  ███░░███   ░░░███░   ░░███░░███ ░░░░░███ ░░███ ░░███  ███░░███ ░███ 
                ░███     ░███ ░░░  ░███ ░███ ░███████      ░███     ░███ ░░░   ███████  ░███  ░███ ░███████  ░███ 
                ░███     ░███      ░███ ░███ ░███░░░       ░███ ███ ░███      ███░░███  ░░███ ███  ░███░░░   ░███ 
                █████    █████     ░░████████░░██████      ░░█████  █████    ░░████████  ░░█████   ░░██████  █████
               ░░░░░    ░░░░░       ░░░░░░░░  ░░░░░░        ░░░░░  ░░░░░      ░░░░░░░░    ░░░░░     ░░░░░░  ░░░░░  

        """
    )
    # menu
    print("Que desea hacer?")
    print("1. Crear")
    print("2. Reservar")
    print("3. Consultar")
    print("x. Salir")

    # variable de control de opciones
    comand = input()

    # Crear
    if comand == "1":

        print("Que desea crear?")
        print("1. Cliente")

        comand = input()

        #Crear cliente
        if comand == "1":
            interfazCrearCliente()

    elif comand == "2":
        print("Reservando")
    #Consultando
    elif comand == "3":

        print("Que desea consultar?")
        print("1. Cliente")
        comand = input()
        
        #Consultar cliente
        if comand == "1":
            interfazListarClientes()

    elif comand == "x":
        break
    else:
        print("Opcion no valida")
        input("Presione enter para volver al menu")
        continue

print("Gracias por usar True Travel")