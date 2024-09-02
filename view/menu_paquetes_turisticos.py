from utils.utils import limpiar_consola, mostrar_banner

def menu_paquetes_turisticos(hotel_service, vuelo_service, paquete_service):
    while True:
        limpiar_consola()
        mostrar_banner()
        print("\n--- Menú Paquetes Turísticos ---")
        print("1. Agregar Paquete Turístico")
        print("2. Buscar Paquete por Destino")
        print("3. Buscar Paquete por ID")
        print("4. Volver al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                destino = input("Ingrese el destino del paquete: ")
                hotel = hotel_service.buscarHotel(int(input("Ingrese el ID del hotel asociado: ")))
                if not hotel:
                    print("Hotel no encontrado.")
                    input("\nPresione Enter para continuar...")
                    continue

                vuelo = vuelo_service.buscarVuelo(int(input("Ingrese el ID del vuelo asociado: ")))
                if not vuelo:
                    print("Vuelo no encontrado.")
                    input("\nPresione Enter para continuar...")
                    continue
                
                diasEstancia = int(input("Ingrese la cantidad de dias de estancia: "))

                paquete = paquete_service.agregarPaqueteTuristico(destino=destino, hotel=hotel, vuelo=vuelo, diasEstancia=diasEstancia)
                print(f"Paquete agregado: {paquete.id} - {paquete.destino} - Hotel: {paquete.hotel.nombre} - Vuelo ID: {paquete.vuelo.id} - precio: {paquete.precio} por {paquete.diasEstancia} días de estancia")
                input("\nPresione Enter para continuar...")
            except Exception as e:
                print("Error al agregar el paquete turístico " + str(e))
                input("\nPresione Enter para continuar...")

        elif opcion == "2":
            try:
                destino = input("Ingrese el destino del paquete: ")
                paquetes = paquete_service.buscarPaqueteTuristico(destino=destino)
                if paquetes:
                    for paquete in paquetes:
                        print(f"{paquete.id} - {paquete.destino} - Hotel: {paquete.hotel.nombre} - Vuelo ID: {paquete.vuelo.id}")
                else:
                    print("No se encontraron paquetes turísticos.")
                input("\nPresione Enter para continuar...")
            except Exception as e:
                print("Error al buscar el paquete turístico " + str(e))
                input("\nPresione Enter para continuar...")

        elif opcion == "3":
            try:
                id_paquete = int(input("Ingrese el ID del paquete turístico: "))
                paquete = paquete_service.buscarPaqueteTuristico(id_paquete)
                if paquete:
                    print(f"Paquete Turístico encontrado: {paquete.id} - {paquete.destino} - Hotel: {paquete.hotel.nombre} - Vuelo ID: {paquete.vuelo.id}")
                else:
                    print("Paquete turístico no encontrado.")
                input("\nPresione Enter para continuar...")
            except Exception as e:
                print("Error al buscar el paquete turístico " + str(e))
                input("\nPresione Enter para continuar...")
                
        elif opcion == "4":
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            input("\nPresione Enter para continuar...")