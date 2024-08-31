from model.vuelo import vuelo
class vuelo_service:

    def __init__(self):
        self.vuelos = [
            vuelo("Lima", "Cusco"),
            vuelo("Cusco", "Lima"),
            vuelo("bogota", "lima"),
            vuelo("lima", "bogota")
        ]

    def agregarVuelo(self, origen, destino):
            
        for vuelo in self.vuelos:
            if vuelo.origen == origen and vuelo.destino == destino:
                    print("El vuelo ya existe")
                    return
            
        newVuelo = vuelo(origen, destino)
        self.vuelos.append(newVuelo)
        print("Vuelo creado con éxito")

        return

    def buscarVuelo(self, origen=None, destino=None):
        # Lista para almacenar los vuelos encontrados
        vuelos_encontrados = []
            
        # Buscar por origen y destino
        if origen and destino:
            vuelos_encontrados = [vuelo for vuelo in self.vuelos if vuelo.origen.lower() == origen.lower() and vuelo.destino.lower() == destino.lower()]
            
        # Buscar solo por origen
        elif origen:
            vuelos_encontrados = [vuelo for vuelo in self.vuelos if vuelo.origen.lower() == origen.lower()]
            
        # Buscar solo por destino
        elif destino:
            vuelos_encontrados = [vuelo for vuelo in self.vuelos if vuelo.destino.lower() == destino.lower()]
            
        # Si no se especifica ni origen ni destino, mostrar todos los vuelos
        else:
            vuelos_encontrados = self.vuelos
            
        # Verificar si se encontraron vuelos
        if vuelos_encontrados:
            print(f"Se encontraron {len(vuelos_encontrados)} vuelo(s):")
            for vuelo in vuelos_encontrados:
                print(f"ID: {vuelo.id}, Origen: {vuelo.origen}, Destino: {vuelo.destino}")
        else:
            print("No se encontraron vuelos con los criterios de búsqueda.")
            
        return vuelos_encontrados