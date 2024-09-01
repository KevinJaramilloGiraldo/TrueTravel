from model.vuelo import Vuelo

class VueloService:

    def __init__(self):
        self.vuelos = [
            Vuelo("Lima", "Cusco", 1800000),
            Vuelo("Cusco", "Lima", 1800000),
            Vuelo("bogota", "lima", 2000000),
            Vuelo("lima", "bogota", 2000000)
        ]

    def agregarVuelo(self, origen, destino, precioIdaYVuelta):
        for vuelo in self.vuelos:
            if vuelo.origen == origen and vuelo.destino == destino and vuelo.precioIdaYVuelta == precioIdaYVuelta:
                return vuelo
            
        newVuelo = Vuelo(origen, destino, precioIdaYVuelta)
        self.vuelos.append(newVuelo)
        return newVuelo

    def buscarVuelo(self, id=None, origen=None, destino=None, precioIdaYVuelta=None):
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
        
        elif precioIdaYVuelta:
            vuelos_encontrados = [vuelo for vuelo in self.vuelos if vuelo.precioIdaYVuelta == precioIdaYVuelta]
        # Si no se especifica ni origen ni destino, mostrar todos los vuelos
        elif id:
            vuelos_encontrados = [vuelo for vuelo in self.vuelos if vuelo.id == id]
            
        else:
            vuelos_encontrados = self.vuelos
        
        # Verificar si se encontraron vuelos
        if vuelos_encontrados:
            return vuelos_encontrados
        else:
            return None
