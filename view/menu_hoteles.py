from utils.utils import limpiar_consola, mostrar_banner


def menu_hoteles(hotel_service):
    while True:
        limpiar_consola()
        mostrar_banner()
        print("\n--- Menú Hoteles ---")
        print("1. Agregar Hotel")
        print("2. Buscar Hotel por Nombre")
        print("3. Buscar Hotel por ID")
        print("4. Volver al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                nombre = input("Ingrese el nombre del hotel: ")
                precio = int(input("Ingrese el precio por noche: "))
                hotel = hotel_service.agregarHotel(nombre, precio)
                print(f"Hotel agregado: {hotel.id} - {hotel.nombre} - Precio por noche: {hotel.precioPorNoche}")
                input("\nPresione Enter para continuar...")
            except Exception as e:
                print("Error al agregar el hotel. Por favor, intente de nuevo." + str(e))
                input("\nPresione Enter para continuar...")

        elif opcion == "2":
            try:
                nombre = input("Ingrese el nombre del hotel: ")
                hoteles = hotel_service.buscarHotel(nombre=nombre)
                if hoteles:
                    for hotel in hoteles:
                        print(f"{hotel.id} - {hotel.nombre} - Precio por noche: {hotel.precioPorNoche}")
                else:
                    print("No se encontraron hoteles.")
                input("\nPresione Enter para continuar...")
            except Exception as e:
                print("Error al buscar el hotel. Por favor, intente de nuevo." + str(e))
                input("\nPresione Enter para continuar...")

        elif opcion == "3":
            try:
                id_hotel = int(input("Ingrese el ID del hotel: "))
                hotel = hotel_service.buscarHotel(id=id_hotel)
                if hotel:
                        print(f"Hotel encontrado: {hotel.id} - {hotel.nombre} - Precio por noche: {hotel.precioPorNoche}")
                else:
                    print("Hotel no encontrado.")
                input("\nPresione Enter para continuar...")
            except Exception as e:
                print("Error al buscar el hotel. Por favor, intente de nuevo." + str(e))
                input("\nPresione Enter para continuar...")

        elif opcion == "4":
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            input("\nPresione Enter para continuar...")