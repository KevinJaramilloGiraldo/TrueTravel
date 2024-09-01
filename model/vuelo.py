class Vuelo:
    _id_counter = 1
    def __init__(self, origen, destino):
        self.id = Vuelo._id_counter
        self.origen = origen
        self.destino = destino

        Vuelo._id_counter += 1