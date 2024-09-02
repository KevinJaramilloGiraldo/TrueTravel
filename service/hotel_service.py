from model.hotel import Hotel

class HotelService:
    def __init__(self):
        
        self.hoteles = [
            Hotel("Hilton", 180000),
            Hotel("Sheraton", 140000),
            Hotel("Hotel Bolivar", 600000),
            Hotel("Casa Blanca", 1300000)
        ]
    def agregarHotel(self, nombre, precioPorNoche):
        for hotel in self.hoteles:
            if hotel.nombre == nombre: 
                return hotel
                
        newHotel = Hotel(nombre,precioPorNoche)
        self.hoteles.append(newHotel)      
        return newHotel

    def buscarHotel(self, id=None, nombre=None):
        # Lista para almacenar los hoteles encontrados
        hoteles_encontrados = []
        
        # Buscar solo por nombre
        if nombre:
            hoteles_encontrados = [hotel for hotel in self.hoteles if hotel.nombre.lower() == nombre.lower()]
        # Buscar solo por id
        elif id:
            hoteles_encontrados = [hotel for hotel in self.hoteles if hotel.id == id]
            if hoteles_encontrados:
                hoteles_encontrados = hoteles_encontrados[0]
        # Si no se especifica mostrar todos los hoteles
        else:
            hoteles_encontrados = self.hoteles
        
        # Verificar si se encontraron hoteles
        if hoteles_encontrados:
            return hoteles_encontrados
        else:
            return None


