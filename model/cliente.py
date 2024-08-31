class cliente:
    # Variable de clase para el contador de IDs
    _id_counter = 1
    
    def __init__(self, nombre, apellido):
        self.id = cliente._id_counter
        self.nombre = nombre
        self.apellido = apellido
        
        # Incrementar el contador de IDs para el siguiente cliente
        cliente._id_counter += 1