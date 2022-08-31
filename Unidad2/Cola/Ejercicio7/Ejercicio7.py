import numpy as np
class Cola:
    __arreglo=None
    __tamaño: int
    __tope=0

    def __init__(self, tamaño: int= 100):
        self.__arreglo=np.empty(tamaño, dtype=Cliente)
        self.__tamaño= tamaño
        self.__tope= 0


    def insertar(self, dato):
        if self.__tope== self.__tamaño:
            raise Exception('Cola llena')

        self.__arreglo[self.__tope]= dato
        self.__tope+=1

    def tamaño(self):
        return self.__tope

    def vacia(self):
        return self.__tope==0

    def eliminar(self):
        if self.__tope==0:
            raise Exception('Cola vacia')

        valor=self.__arreglo[0]
        for i in range(1, self.__tope):
            self.__arreglo[i-1]= self.__arreglo[i]

        self.__tope-=1

        return valor


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




