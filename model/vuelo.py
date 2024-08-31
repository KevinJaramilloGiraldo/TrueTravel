class vuelo:
    _id_counter = 1
    def __init__(self, origen, destino):
        self.id = vuelo._id_counter
        self.origen = origen
        self.destino = destino

        vuelo._id_counter += 1