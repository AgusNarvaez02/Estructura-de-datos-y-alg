import numpy as np

class Torre:
    __arreglo=None
    __tope=0
    __tamaño: int

    def __init__(self, tamaño: int=3):
        self.__arreglo= np.empty(tamaño, dtype=int)
        self.__tope= 0
        self.__tamaño=tamaño

    def vacio(self):
        return self.__tope==0

    def añadirDisco(self, elemento):
        if self.vacio() or elemento<= self.__arreglo[self.__tope-1]:
            print('ingresa al if')
            self.__arreglo[self.__tope]=elemento
            self.__tope+=1
        else:
            print('No puede colocar un disco mas grande encima de uno mas pequeño ')
            raise Exception('No puede colocar un disco mas grande encima de uno mas pequeño ')

    def tamaño(self):
        return self.__tope


    def eliminarvalor(self):
        if self.__tope==0:
            raise Exception('Pila vacia')

        self.__tope-=1
        return self.__arreglo[self.__tope]

    def TamañoDisco(self, i):
        if self.__tope<i:
            return ' '

        return str(self.__arreglo[i-1])

