from model.hotel import hotel


class hotel_service:
    def __init__(self):
        self.hoteles = [
            hotel("Hilton", "Lima"),
            hotel("Sheraton", "Cusco"),
            hotel("Hotel Bolivar", "Bogota"),
            hotel("Casa Blanca", "Lima"),
        ]
    def agregarHotel(self, nombre, ciudad):

        for hotel in self.hoteles:
            if hotel.nombre == nombre and hotel.ciudad == ciudad:
                    print ("El hotel ya existe")
                    return
                
        newHotel = hotel(nombre,ciudad)
        self.hoteles.append(newHotel)
        print ("Hotel creado con éxito")
        
        return

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
            print(f"Se encontraron {len(hoteles_encontrados)} hotel(es):")
            for hotel in hoteles_encontrados:
                print(f"ID: {hotel.id}, Nombre: {hotel.nombre}, Ciudad: {hotel.ciudad}")
        else:
            print("No se encontraron hoteles con los criterios de búsqueda.")
        
        return hoteles_encontrados