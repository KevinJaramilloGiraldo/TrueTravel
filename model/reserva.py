import datetime

class Reserva:
    _id_counter = 1
    def __init__(self, cliente, paquete_turistico, fecha_ida):
        self.id = Reserva._id_counter
        self.cliente = cliente
        self.paquete_turistico = paquete_turistico
        self.fecha_ida = fecha_ida
        self.vuelos = paquete_turistico.vuelo
        self.fecha_regreso = fecha_ida + datetime.timedelta(days=paquete_turistico.diasEstancia)
        Reserva._id_counter += 1
