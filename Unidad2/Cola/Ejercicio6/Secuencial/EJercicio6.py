import numpy as np
class Cola:
    __arreglo=None
    __tamaño: int
    __tope=0

    def __init__(self, tamaño: int= 20):
        self.__arreglo=np.empty(tamaño, dtype=int)
        self.__tamaño= tamaño
        self.__tope= 0


    def insertar(self, dato):
        if self.__tope== self.__tamaño:
            raise Exception('Cola llena')

        self.__arreglo[self.__tope]= dato
        self.__tope+=1

    def tamaño(self):
        return self.__tope

    def eliminar(self):
        if self.__tope==0:
            raise Exception('Cola vacia')

        valor=self.__arreglo[0]
        for i in range(1, self.__tope):
            self.__arreglo[i-1]= self.__arreglo[i]

        self.__tope-=1

        return valor


if __name__ == '__main__':
    c=Cola()
    c.insertar(1)
    c.insertar(2)
    c.insertar(3)
    c.insertar(4)
    c.insertar(5)
    print(c.eliminar())
