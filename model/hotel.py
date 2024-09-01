class Hotel:
    _id_counter = 1
    def __init__(self, nombre, ciudad):
        self.id = Hotel._id_counter
        self.nombre = nombre
        self.ciudad = ciudad

        Hotel._id_counter += 1