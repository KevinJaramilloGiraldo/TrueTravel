class Reserva:
    _id_counter = 1
    def __init__(self, cliente, vuelo_ida, vuelo_regreso, hotel):
        self.id = Reserva._id_counter
        self.cliente = cliente
        self.vuelo_ida = vuelo_ida
        self.vuelo_regreso = vuelo_regreso
        self.hotel = hotel

        Reserva._id_counter += 1
