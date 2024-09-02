from service.cliente_service import ClienteService
from service.hotel_service import HotelService
from service.paquete_turistico_service import PaqueteTuristicoService
from service.reserva_service import ReservaService
from service.vuelo_service import VueloService
from utils.utils import limpiar_consola, mostrar_banner
from view.menu_clientes import menu_clientes
from view.menu_hoteles import menu_hoteles
from view.menu_paquetes_turisticos import menu_paquetes_turisticos
from view.menu_reservas import menu_reservas
from view.menu_vuelos import menu_vuelos

# Inicialización de los servicios
cliente_service = ClienteService()
hotel_service = HotelService()
vuelo_service = VueloService()
paquete_service = PaqueteTuristicoService()
reserva_service = ReservaService()

def menu_principal():
    while True:
        limpiar_consola()
        mostrar_banner()

        print("\n--- Menú Principal sd---")
        print("1. Clientes")
        print("2. Hoteles")
        print("3. Vuelos")
        print("4. Paquetes Turísticos")
        print("5. Reservas")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menu_clientes(cliente_service)
        elif opcion == "2":
            menu_hoteles(hotel_service)
        elif opcion == "3":
            menu_vuelos(vuelo_service)
        elif opcion == "4":
            menu_paquetes_turisticos(hotel_service, vuelo_service, paquete_service)
        elif opcion == "5":
            menu_reservas(reserva_service, cliente_service, paquete_service)
        elif opcion == "6":
            limpiar_consola()
            print("Gracias por usar TrueTravel. ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Inicia el menú principal
menu_principal()