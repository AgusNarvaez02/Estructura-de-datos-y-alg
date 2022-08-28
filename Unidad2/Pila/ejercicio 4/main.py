import numpy as np
from numpy import array
class Pila:
    __arreglo=array
    __tope1= 0
    __tope2= 0

    def __init__(self):
        self.__arreglo= np.empty(100,int)
        self.__tope1=0
        self.__tope2=99

    def insertar(self, dato):
        if (self.__tope1 - self.__tope2)==-1:
            raise Exception('Pila llena')
        self.__arreglo[self.__tope1]=dato
        self.__tope1+=1

    def insertarFinal(self, dato):
        if (self.__tope1 - self.__tope2)==-1:
            raise Exception('Pila llena')

        self.__arreglo[self.__tope2]=dato
        self.__tope2-=1

    def tamaño1(self):
        return self.__tope1

    def tamaño2(self):
        return 99-self.__tope2

    def eliminar1(self):
        if self.__tope1==0:
            raise Exception('pila vacia')
        self.__tope1-=1
        valor = self.__arreglo[self.__tope1]
        return valor

    def eliminar2(self):
        if self.__tope2==99:
            raise Exception('pila vacia')
        self.__tope2+=1
        valor = self.__arreglo[self.__tope2]
        return valor

if __name__ == '__main__':
    pila=Pila()
    pila.insertarFinal(5)
    pila.insertarFinal(4)
    pila.insertarFinal(3)
    print(pila.eliminar2())
