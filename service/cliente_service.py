from model.cliente import Cliente #importar la clase con la que trabajan los metodos
class ClienteService:
#Metodo constructor
    def __init__(self):
        self.clientes = [
            Cliente("Juan", "Perez"),
            Cliente("Maria", "Gonzalez"),
            Cliente("Pedro", "Lopez"),
            Cliente("Ana", "Martinez")
        ]

    def agregarClientes (self, nombre, apellido):

        for cliente in self.clientes:
            if cliente.nombre==nombre and cliente.apellido==apellido:
                    return cliente
        newCliente= Cliente(nombre,apellido)
        self.clientes.append(newCliente)
        return newCliente
    
    def buscarClientesPorNombreYApellido (self, nombre=None, apellido=None):
        #Lista para almacenar los clientes encontrados
        clientes_Encontrados=[]
        #Ciclo para buscar los clientes
        if nombre and apellido:
            clientes_Encontrados=[clientes for clientes in self.clientes if clientes.nombre.lower()==nombre.lower() and clientes.apellido.lower()==apellido.lower()]
            return clientes_Encontrados
        elif  nombre:
            clientes_Encontrados=[clientes for clientes in self.clientes if clientes.nombre.lower()==nombre.lower()]
            return clientes_Encontrados
        elif apellido:
            clientes_Encontrados=[clientes for clientes in self.clientes if clientes.apellido.lower()==apellido.lower()]
            return clientes_Encontrados
        else:
            return None

    def buscarClientesPorID (self, id):
        for cliente in self.clientes:
            if cliente.id==id:
                    return cliente
        return None