import numpy as np
class Nodo:
    __dato=None
    __siguiente:int


    def __int__(self, dato, sig):
        self.__dato=dato
        self.__siguiente=sig

    def getDato(self):
        return self.__dato

    def SerDato(self, dato):
        self.__dato=dato
    def setSig(self, siguiente):
        self.__siguiente= siguiente

    def getSig(self):
        return self.__siguiente



class Lista:
    __arreglo= np.ndarray
    __inicio: int
    __inicioVacio: int
    __CantElem: int



    def __init__(self, tamaño: int=100):
        self.__arreglo= np.empty(tamaño, dtype= Nodo)
        self.__inicio=-1
        self.__inicioVacio=0
        self.__CantElem= 0

        for i in range(tamaño-1):
            self.__arreglo[i]= Nodo(None, i+1)

        self.__arreglo[tamaño-1]= Nodo(None, -1)

    def getTamaño(self):
        return self.__CantElem

    def Vacia(self):
        return self.__inicio=-1

    def Insertar(self, pos, dato):
        if self.__inicioVacio==-1:
            raise Exception('Lista Llena')

        posElemento= self.__inicioVacio
        elem= self.__arreglo[posElemento]
        elem.setDato(dato)
        self.__inicioVacio= elem.getSig()

        if pos==0:
            elem.setSig(self.__inicio)
            self.__inicio=posElemento

        else:
            ant= self.Recup(pos-1)
            elem.setSig(ant.getSig())
            ant.setSig(posElemento)

        self.__CantElem+=1

    def Eliminar(self, pos):
        if 0>pos>self.__CantElem:
            raise Exception('Posicion no Valida')

        if pos==0:
            aux= self.__inicio
            self.__inicio= self.__arreglo[aux].getSig()
            self.__arreglo[aux].setSig(self.__inicioVacio)
            self.__inicioVacio=aux

        else:
            ant = self.Recup(pos - 1)
            aux= ant.getSig()
            ant.setSig(self.__arreglo[aux].getSig())
            self.__arreglo[aux].setSig(self.__inicioVacio)
            self.__inicioVacio=aux

    def primerElem(self):
        if self.Vacia():
            raise Exception('Lista vacia')
        elem= self.__arreglo[self.__inicio].getDato()
        return elem

    def UltimoElem(self):
        if self.Vacia():
            raise Exception('Lista vacia')

        return self.Recup(self.__CantElem-1)

    def Recup(self, pos):
        aux= self.__inicio

        while pos!=0:
            aux= self.__arreglo[aux].getSig()
            pos-=1
        return self.__arreglo[aux]


    def Recuperar(self, pos):
        return self.Recup(pos).getDato()


if __name__ == '__main__':
    lis=Lista()
    lis.Insertar(0, 2)
    lis.Insertar(1, 4)

