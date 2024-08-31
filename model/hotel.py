class hotel:
    _id_counter = 1
    def __init__(self, nombre, ciudad):
        self.id = hotel._id_counter
        self.nombre = nombre
        self.ciudad = ciudad

        hotel._id_counter += 1