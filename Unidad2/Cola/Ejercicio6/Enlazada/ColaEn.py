class Nodo:
    __dato=str
    __siguiente=None


    def __init__(self, dato):
        self.__dato= dato
        self.__siguiente=None


    def getdato(self):
        return self.__dato

    def setsig(self, dat):
        self.__siguiente=dat

    def getsig(self):
        return self.__siguiente


class Cola:
    __tamaño=0
    __cabeza=None
    __cola=None

    def __init__(self):
        self.__cabeza = None
        self.__tamaño = 0
        self.__cola=None

    def ingresar(self, dato):
        nodo = Nodo(dato)
        if self.__cabeza==None:
            self.__cabeza=nodo
            self.__cola=nodo
        else:
            self.__cola.setsig(nodo)
            self.__cola = nodo

    def tamaño(self):
        return self.__tamaño

    def eliminar(self):
        if self.__cabeza == None:
            raise Exception('Cabeza vacia')
        aux = self.__cabeza
        self.__cabeza = self.__cabeza.getsig()
        return aux.getdato()


if __name__ == '__main__':
    ob = Cola()
    ob.ingresar('FabriCapo')
    ob.ingresar('Aguss')
    print(ob.eliminar())