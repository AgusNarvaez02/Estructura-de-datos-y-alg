class Cola:
    __lista = None

    def __init__(self):
        self.__lista = []

    def insertar(self, dato):
        self.__lista.append(dato)

    def tamaño(self):
        return len(self.__lista)

    def eliminar(self):
        if len(self.__lista) == 0:
            raise Exception('Lista vacia')
        return self.__lista.pop(0)

    def vacia(self):
        return len(self.__lista)==0


class Cliente:
    __id: int

    def __init__(self, id):
        self.__id=id

    def getid(self):
        return self.__id

class Cajero:
    __ocupado: bool
    __cliente: Cliente

    def __init__(self):
        self.__ocupado= False
        self.__cliente= None


    def esta_ocupado(self):
        return self.__ocupado

    def Atencion(self, cliente):
        self.__cliente= cliente
        self.__ocupado=True

    def ClientefueAtendido(self):
        self.__cliente=None
        self.__ocupado=False




if __name__ == '__main__':
    cola=Cola()
    cajero=Cajero()
    TiempodeSimulacion= int(input('Ingrese tiempo de simulacion: '))
    tiempodeAtencionCajero = int(input('Ingrese tiempo de atencion de cajero: '))
    tiempodeFrecuenciadeCliente = int(input('Ingrese tiempo de frecuencia de llegada de clientes: '))
    tiempoTranscurrido= 0
    clientes=0
    tiempodeEspera=0

    while tiempoTranscurrido <=TiempodeSimulacion:
        tiempodeEspera+=cola.tamaño()

        if (tiempoTranscurrido % tiempodeFrecuenciadeCliente)==0:
            clientes+=1
            cola.insertar(Cliente(clientes))
        if (tiempoTranscurrido % tiempodeAtencionCajero) == 0 and not cola.vacia():
            clien= cola.eliminar()
            cajero.Atencion(clien)
            print('Se atendio al cliente numero: {}'.format(clien.getid()))

        tiempoTranscurrido+=1

    prom= tiempodeEspera/clientes

    print('EL tiempo de espera promedio es: {:.2f} minutos'.format((prom)))



