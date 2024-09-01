from model.paquete_turistico import PaqueteTuristico

class PaqueteTuristicoService:
    def __init__(self):
        
        self.paquetes_turisticos = []
        
    def agregarPaqueteTuristico (self, destino, hotel, vuelo, diasEstancia):
        
        for paquete_turistico in self.paquetes_turisticos:
            if paquete_turistico.destino == destino and paquete_turistico.diasEstancia == diasEstancia and paquete_turistico.hotel == hotel:
                return paquete_turistico
            
        newPaqueteTuristico = PaqueteTuristico(destino, hotel, vuelo,diasEstancia)
        self.paquetes_turisticos.append(newPaqueteTuristico)
        return newPaqueteTuristico
    
    def buscarPaqueteTuristico (self, id=None, destino=None, diasEstancia=None):
        # Lista para almacenar los paquetes encontrados
        paquetesTuristicosEncontrados = []
        
        # Buscar por destino y dias de estancia 
        if destino and diasEstancia:
            paquetesTuristicosEncontrados = [paquete_turistico for paquete_turistico in self.paquetes_turisticos if paquete_turistico.destino.lower() == destino.lower() and paquete_turistico.diasEstancia == diasEstancia]
        
        # Buscar solo por destino
        elif destino:
            paquetesTuristicosEncontrados = [paquete_turistico for paquete_turistico in self.paquetes_turisticos if paquete_turistico.destino.lower() == destino.lower()]
        
        # Buscar solo por dias de estancia
        elif diasEstancia:
            paquetesTuristicosEncontrados = [paquete_turistico for paquete_turistico in self.paquetes_turisticos if paquete_turistico.diasEstancia == diasEstancia]
        
        elif id:
            paquetesTuristicosEncontrados = [paquete_turistico for paquete_turistico in self.paquetes_turisticos if paquete_turistico.id == id]
        # Si no se especifica ni destino ni dias de estancia, mostrar todos los paquetes
        else:
            paquetesTuristicosEncontrados = self.paquetes_turisticos
        
        # Verificar si se encontraron paquetes
        if paquetesTuristicosEncontrados:
            return paquetesTuristicosEncontrados
        else:
            return None 