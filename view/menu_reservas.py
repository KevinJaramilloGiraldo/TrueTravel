import datetime
from utils.utils import limpiar_consola, mostrar_banner

def menu_reservas(reserva_service, cliente_service, paquete_service):
    while True:
        limpiar_consola()
        mostrar_banner()
        print("\n--- Menú Reservas ---")
        print("1. Realizar Reserva")
        print("2. Buscar Reserva por ID")
        print("3. Volver al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                cliente = cliente_service.buscarClientesPorID(int(input("Ingrese el ID del cliente: ")))
                paquete = paquete_service.buscarPaqueteTuristico(int(input("Ingrese el ID del paquete turístico: ")))
                fecha = input("Ingrese la fecha de la reserva (YYYY-MM-DD): ")
                fecha_reserva = datetime.datetime.strptime(fecha, "%Y-%m-%d")
                reserva = reserva_service.agregarReserva(cliente, paquete, fecha_reserva)
                print(f"Reserva realizada: {reserva.id} - Cliente : {reserva.cliente.nombre} - fecha vuelo {reserva.fecha_ida} fecha regreso {reserva.fecha_regreso}")
                input("\nPresione Enter para continuar...")
            except Exception as e:
                print("Opción no válida. Por favor, intente de nuevo." + str(e))
                input("\nPresione Enter para continuar...")

        elif opcion == "2":
            try:
                id_reserva = int(input("Ingrese el ID de la reserva: "))
                reserva = reserva_service.buscarReservas(id_reserva)
                if reserva:
                    print(f"Reserva encontrada: {reserva.id} - Cliente : {reserva.cliente.nombre} - Paquete ID: {reserva.paquete_turistico.id} - Fecha vuelo {reserva.fecha_ida} Fecha regreso {reserva.fecha_regreso}")
                else:
                    print("Reserva no encontrada.")
                input("\nPresione Enter para continuar...")
            except Exception as e:
                print("Opción no válida. Por favor, intente de nuevo. " + str(e))
                input("\nPresione Enter para continuar...")

        elif opcion == "3":
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            input("\nPresione Enter para continuar...")