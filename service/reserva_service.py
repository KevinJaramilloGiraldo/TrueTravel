from model.reserva import Reserva

class ReservaService:
    def __init__(self):
        self.reservas = []

    def agregarReserva(self, cliente, paqueteTuristico, fecha_ida, vuelo_origen):
        
        for reserva in self.reservas:
            if reserva.cliente == cliente and reserva.paquete_turistico == paqueteTuristico and reserva.fecha_ida == fecha_ida:
                return reserva
        reserva = Reserva(cliente, paqueteTuristico, fecha_ida,vuelo_origen)
        self.reservas.append(reserva)   
        return  reserva
            
    def buscarReservas(self, id=None, cliente=None, paqueteTuristico=None, fecha_ida=None):
        
        reservas_encontradas = []

        if cliente:
            reservas_encontradas = [reserva for reserva in self.reservas if reserva.cliente == cliente]

        elif paqueteTuristico:
            reservas_encontradas = [reserva for reserva in self.reservas if reserva.paquete_turistico == paqueteTuristico]
        
        elif id:
            reservas_encontradas = [reserva for reserva in self.reservas if reserva.id == id]
        
        else:
            return reservas_encontradas
        return None