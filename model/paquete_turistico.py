class PaqueteTuristico:
    _id_counter = 1
    def __init__(self, ciudad, vuelo_ida, vuelo_regreso, hotel):
        self.ciudad = ciudad
        self.vuelo_ida = vuelo_ida
        self.vuelo_regreso = vuelo_regreso
        self.hotel = hotel

        PaqueteTuristico._id_counter += 1