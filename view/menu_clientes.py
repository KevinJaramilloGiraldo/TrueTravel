from utils.utils import limpiar_consola, mostrar_banner

def menu_clientes(cliente_service):
    while True:
        limpiar_consola()
        mostrar_banner()
        print("\n--- Menú Clientes ---")
        print("1. Agregar Cliente")
        print("2. Buscar Cliente por Nombre/Apellido")
        print("3. Buscar Cliente por ID")
        print("4. Volver al Menú Principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                nombre = input("Ingrese el nombre del cliente: ")
                apellido = input("Ingrese el apellido del cliente: ")
                cliente = cliente_service.agregarClientes(nombre, apellido)
                print(f"Cliente agregado: {cliente.id} - {cliente.nombre} {cliente.apellido}")
                input("\nPresione Enter para continuar...")
            except Exception as e:
                print("Error al agregar el cliente. Por favor, intente de nuevo." + str(e))
                input("\nPresione Enter para continuar...")

        elif opcion == "2":
            try:
                nombre = input("Ingrese el nombre del cliente (o deje vacío): ")
                apellido = input("Ingrese el apellido del cliente (o deje vacío): ")
                clientes = cliente_service.buscarClientesPorNombreYApellido(nombre, apellido)
                if clientes:
                    for cliente in clientes:
                        print(f"{cliente.id} - {cliente.nombre} {cliente.apellido}")
                else:
                    print("No se encontraron clientes.")
                input("\nPresione Enter para continuar...")
            except Exception as e:
                print("Error al buscar el cliente. Por favor, intente de nuevo." + str(e))
                input("\nPresione Enter para continuar...")

        elif opcion == "3":
            try:
                id_cliente = int(input("Ingrese el ID del cliente: "))
                cliente = cliente_service.buscarClientesPorID(id_cliente)
                if cliente:
                    print(f"Cliente encontrado: {cliente.id} - {cliente.nombre} {cliente.apellido}")
                else:
                    print("Cliente no encontrado.")
                input("\nPresione Enter para continuar...")
            except Exception as e:
                print("Error al buscar el cliente. Por favor, intente de nuevo." + str(e))
                input("\nPresione Enter para continuar...")

        elif opcion == "4":
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            input("\nPresione Enter para continuar...")