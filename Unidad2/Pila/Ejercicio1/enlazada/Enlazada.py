class Nodo:
    __next= None
    __dato= None


    def __init__(self, dato):
        self.__dato=dato
        self.__next= None

    def setnext(self, sig):
        self.__next= sig

    def getnetx(self):
        return self.__next
    def getdato(self):
        return self.__dato
