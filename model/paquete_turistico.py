class PaqueteTuristico:
    _id_counter = 1
    def __init__(self, destino, hotel, vuelo, diasEstancia):
        self.id = PaqueteTuristico._id_counter
        self.destino = destino
        self.diasEstancia = int(diasEstancia)
        self.vuelo = vuelo
        self.hotel = hotel
        self.precio = self.hotel.precioPorNoche * self.diasEstancia + self.vuelo.precioIdaYVuelta
        PaqueteTuristico._id_counter += 1