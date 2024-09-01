class Hotel:
    _id_counter = 1
    def __init__(self, nombre, precioPorNoche):
        self.id = Hotel._id_counter
        self.nombre = nombre
        self.precioPorNoche = int(precioPorNoche)

        Hotel._id_counter += 1

