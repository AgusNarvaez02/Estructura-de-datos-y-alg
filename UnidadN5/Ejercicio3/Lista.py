class Nodo:
    __dato=None
    __siguiente= None

    def __init__(self, dato):
        self.__dato=dato
        self.__siguiente=None
    def getdato(self):
        return self.__dato
    def setdato(self, dato):
        self.__dato=dato

    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente


    def getSiguiente(self):
       return self.__siguiente


class Lista:
    __cabeza:Nodo
    __cola:Nodo
    __tamaño: int

    def __init__(self):
        self.__cabeza=None
        self.__cola=None
        self.__tamaño=0

    def getTamaño(self):
        return self.__tamaño
    def Vacio(self):
        return self.__cabeza==None

    def insertar(self, dato):
        nuevo= Nodo(dato)
        if self.Vacio():
            self.__cabeza=nuevo
            self.__cola=nuevo
        else:
            nodo= self.buscar(dato)
            if nodo==None:
                self.__cola.setSiguiente(nuevo)
                self.__cola=nuevo
            else:
                nodo.setdato(dato)
        self.__tamaño+=1


    def buscar(self, dato):
        aux= self.__cabeza
        while aux!=None:
            if aux.getdato()== dato:
                return aux
            aux= aux.getSiguiente()

        return -1


    def Rrecorrer(self):
        aux= self.__cabeza
        lis= ''
        while aux != None:
            lis+= str(aux.getdato())+'=>'
            aux= aux.getSiguiente()
        lis+='None'
        print(lis)

