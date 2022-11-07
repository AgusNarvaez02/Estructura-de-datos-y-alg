class Nodo:
    __dato= None
    __siguiente=None


    def __init__(self, dato):
        self.__dato=dato
        self.__siguiente=None

    def getDato(self):
        return self.__dato

    def getSiguiente(self):
        return self.__siguiente

    def setSig(self, sig):
        self.__siguiente=sig

    def setDato(self, date):
        self.__dato=date


class Lista:
    __cabeza=Nodo

    def __init__(self):
        self.__cabeza=None

    def Insertar(self, date):
        Nuevo= Nodo(date)
        if self.__cabeza==None:
            self.__cabeza= Nuevo

        elif not self.Relacionado(date):
            Nuevo.setSig(self.__cabeza)
            self.__cabeza=Nuevo

    def Relacionado(self, date):
        aux= self.__cabeza
        rep=False
        while aux!=None and not rep:
            if aux.getDato()==date:
                rep=True

            aux= aux.getSiguiente()
        return rep
