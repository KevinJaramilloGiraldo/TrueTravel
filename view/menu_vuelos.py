from utils.utils import limpiar_consola, mostrar_banner

def menu_vuelos(vuelo_service):
    while True:
        limpiar_consola()
        mostrar_banner()
        print("\n--- Menú Vuelos ---")
        print("1. Agregar Vuelo")
        print("2. Buscar Vuelo por Origen y Destino")
        print("3. Buscar Vuelo por ID")
        print("4. Volver al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                origen = input("Ingrese el origen del vuelo: ")
                destino = input("Ingrese el destino del vuelo: ")
                precio = int(input("Ingrese el precio ida y vuelta: "))
                vuelo = vuelo_service.agregarVuelo(origen, destino, precio)
                print(f"Vuelo agregado: {vuelo.id} - {vuelo.origen} -> {vuelo.destino} - Precio: {vuelo.precioIdaYVuelta}")
                input("\nPresione Enter para continuar...")
            except Exception as e:
                print("Ocurrio un error al agregar el vuelo. Por favor, intente de nuevo." + str(e))
                input("\nPresione Enter para continuar...")

        elif opcion == "2":
            try:
                origen = input("Ingrese el origen del vuelo: ")
                destino = input("Ingrese el destino del vuelo: ")
                vuelos = vuelo_service.buscarVuelo(origen=origen, destino=destino)
                if vuelos:
                    for vuelo in vuelos:
                        print(f"{vuelo.id} - {vuelo.origen} -> {vuelo.destino} - Precio: {vuelo.precioIdaYVuelta}")
                else:
                    print("No se encontraron vuelos.")
                input("\nPresione Enter para continuar...")
            except Exception as e:
                print("Error al buscar el vuelo. Por favor, intente de nuevo." + str(e))
                input("\nPresione Enter para continuar...")

        elif opcion == "3":
            try:
                id_vuelo = int(input("Ingrese el ID del vuelo: "))
                vuelo = vuelo_service.buscarVuelo(id=id_vuelo)
                if vuelo:
                    print(f"Vuelo encontrado: {vuelo.id} - {vuelo.origen} -> {vuelo.destino} - Precio: {vuelo.precioIdaYVuelta}")
                else:
                    print("Vuelo no encontrado.")
                input("\nPresione Enter para continuar...")
            except Exception as e:
                print("Error al buscar el vuelo. Por favor, intente de nuevo." + str(e))
                input("\nPresione Enter para continuar...")

        elif opcion == "4":
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            input("\nPresione Enter para continuar...")