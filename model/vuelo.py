class Vuelo:
    _id_counter = 1
    def __init__(self, origen, destino, precioIdaYVuelta):
        self.id = Vuelo._id_counter
        self.origen = origen
        self.destino = destino
        self.precioIdaYVuelta = int(precioIdaYVuelta)
        
        Vuelo._id_counter += 1