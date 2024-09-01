from model.vuelo import Vuelo

class VueloService:

    def __init__(self):
        self.vuelos = [
            Vuelo("Lima", "Cusco"),
            Vuelo("Cusco", "Lima"),
            Vuelo("bogota", "lima"),
            Vuelo("lima", "bogota")
        ]

    def agregarVuelo(self, origen, destino):
            
        for vuelo in self.vuelos:
            if vuelo.origen == origen and vuelo.destino == destino:
                    return vuelo
            
        newVuelo = Vuelo(origen, destino)
        self.vuelos.append(newVuelo)
        return newVuelo

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
            return vuelos_encontrados
        else:
            return None