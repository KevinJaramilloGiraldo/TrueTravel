from model.cliente import cliente
class cliente_service:

    def __init__(self):
        self.clientes = [
            cliente("Juan", "Perez"),
            cliente("Maria", "Gonzalez"),
            cliente("Pedro", "Lopez"),
            cliente("Ana", "Martinez")
        ]

    def agregarClientes (self, nombre, apellido):

        for cliente in self.clientes:
            if cliente.nombre==nombre and cliente.apellido==apellido:
                    print ("El cliente ya existe")
                    return
        newCliente= cliente(nombre,apellido)
        self.clientes.append(newCliente)
        print ("Cliente creado con exito")
        
        return