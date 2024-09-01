from model.hotel import Hotel

class HotelService:
    def __init__(self):
        
        self.hoteles = [
            Hotel("Hilton", "Lima"),
            Hotel("Sheraton", "Cusco"),
            Hotel("Hotel Bolivar", "Bogota"),
            Hotel("Casa Blanca", "Lima")
        ]
    def agregarHotel(self, nombre, ciudad):

        for hotel in self.hoteles:
            if hotel.nombre == nombre and hotel.ciudad == ciudad:
                return hotel
                
        newHotel = Hotel(nombre,ciudad)
        self.hoteles.append(newHotel)      
        return newHotel

    def buscarHotel(self, nombre=None, ciudad=None):
        # Lista para almacenar los hoteles encontrados
        hoteles_encontrados = []
        
        # Buscar por nombre y ciudad
        if nombre and ciudad:
            hoteles_encontrados = [hotel for hotel in self.hoteles if hotel.nombre.lower() == nombre.lower() and hotel.ciudad.lower() == ciudad.lower()]
        
        # Buscar solo por nombre
        elif nombre:
            hoteles_encontrados = [hotel for hotel in self.hoteles if hotel.nombre.lower() == nombre.lower()]
        
        # Buscar solo por ciudad
        elif ciudad:
            hoteles_encontrados = [hotel for hotel in self.hoteles if hotel.ciudad.lower() == ciudad.lower()]
        
        # Si no se especifica ni nombre ni ciudad, mostrar todos los hoteles
        else:
            hoteles_encontrados = self.hoteles
        
        # Verificar si se encontraron hoteles
        if hoteles_encontrados:
            return hoteles_encontrados
        else:
            return None