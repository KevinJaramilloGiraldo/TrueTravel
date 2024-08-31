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

def crearReserva(cliente_id, vuelo_ida_id, vuelo_regreso_id, hotel_id):
    # Verificar si el cliente existe
    cliente = next((c for c in clientes if c.id == cliente_id), None)
    if not cliente:
        print("El cliente no existe.")
        return
    
    # Verificar si el vuelo de ida existe
    vuelo_ida = next((v for v in vuelos if v.id == vuelo_ida_id), None)
    if not vuelo_ida:
        print("El vuelo de ida no existe.")
        return
    
    # Verificar si el vuelo de regreso existe
    vuelo_regreso = next((v for v in vuelos if v.id == vuelo_regreso_id), None)
    if not vuelo_regreso:
        print("El vuelo de regreso no existe.")
        return
    
    # Verificar si el hotel existe
    hotel = next((h for h in hoteles if h.id == hotel_id), None)
    if not hotel:
        print("El hotel no existe.")
        return
    
    # Crear la reserva
    nueva_reserva = Reserva(cliente, vuelo_ida, vuelo_regreso, hotel)
    reservas.append(nueva_reserva)
    
    print(f"Reserva creada con éxito para {cliente.nombre} {cliente.apellido}.")
    return

def listarReservas():
    if not reservas:
        print("No hay reservas registradas.")
        return
    
    for reserva in reservas:
        print(f"Reserva ID: {reserva.id} - Cliente: {reserva.cliente.nombre} {reserva.cliente.apellido}")
        print(f"  Vuelo de ida: {reserva.vuelo_ida.origen} -> {reserva.vuelo_ida.destino}")
        print(f"  Vuelo de regreso: {reserva.vuelo_regreso.origen} -> {reserva.vuelo_regreso.destino}")
        print(f"  Hotel: {reserva.hotel.nombre} en {reserva.hotel.ciudad}")
        print()

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

def buscarHotel(nombre=None, ciudad=None):
    # Lista para almacenar los hoteles encontrados
    hoteles_encontrados = []
    
    # Buscar por nombre y ciudad
    if nombre and ciudad:
        hoteles_encontrados = [hotel for hotel in hoteles if hotel.nombre.lower() == nombre.lower() and hotel.ciudad.lower() == ciudad.lower()]
    
    # Buscar solo por nombre
    elif nombre:
        hoteles_encontrados = [hotel for hotel in hoteles if hotel.nombre.lower() == nombre.lower()]
    
    # Buscar solo por ciudad
    elif ciudad:
        hoteles_encontrados = [hotel for hotel in hoteles if hotel.ciudad.lower() == ciudad.lower()]
    
    # Si no se especifica ni nombre ni ciudad, mostrar todos los hoteles
    else:
        hoteles_encontrados = hoteles
    
    # Verificar si se encontraron hoteles
    if hoteles_encontrados:
        print(f"Se encontraron {len(hoteles_encontrados)} hotel(es):")
        for hotel in hoteles_encontrados:
            print(f"ID: {hotel.id}, Nombre: {hotel.nombre}, Ciudad: {hotel.ciudad}")
    else:
        print("No se encontraron hoteles con los criterios de búsqueda.")
    
    return hoteles_encontrados

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

def buscarVuelo(origen=None, destino=None):
    # Lista para almacenar los vuelos encontrados
    vuelos_encontrados = []
    
    # Buscar por origen y destino
    if origen and destino:
        vuelos_encontrados = [vuelo for vuelo in vuelos if vuelo.origen.lower() == origen.lower() and vuelo.destino.lower() == destino.lower()]
    
    # Buscar solo por origen
    elif origen:
        vuelos_encontrados = [vuelo for vuelo in vuelos if vuelo.origen.lower() == origen.lower()]
    
    # Buscar solo por destino
    elif destino:
        vuelos_encontrados = [vuelo for vuelo in vuelos if vuelo.destino.lower() == destino.lower()]
    
    # Si no se especifica ni origen ni destino, mostrar todos los vuelos
    else:
        vuelos_encontrados = vuelos
    
    # Verificar si se encontraron vuelos
    if vuelos_encontrados:
        print(f"Se encontraron {len(vuelos_encontrados)} vuelo(s):")
        for vuelo in vuelos_encontrados:
            print(f"ID: {vuelo.id}, Origen: {vuelo.origen}, Destino: {vuelo.destino}")
    else:
        print("No se encontraron vuelos con los criterios de búsqueda.")
    
    return vuelos_encontrados

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