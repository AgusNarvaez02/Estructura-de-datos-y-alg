import numpy as np

class Pila:
    __arreglo=None
    __tope=0
    __tamaño: int

    def __init__(self, tamaño: int=20):
        self.__arreglo= np.empty(tamaño, dtype=int)
        self.__tope= 0
        self.__tamaño=tamaño


    def insertar(self, dato):
        if self.__tope== self.__tamaño:
            raise Exception('Pila llena')

        self.__arreglo[self.__tope]= dato
        self.__tope+=1

    def getTam(self):
        return self.__tope

    def eliminarvalor(self):
        if self.__tope==0:
            raise Exception('Pila vacia')

        self.__tope-=1
        return self.__arreglo[self.__tope]

def conversion(num):
    pila=Pila()
    while num>=1:
        resto = num % 2
        pila.insertar(resto)
        num= num//2
    string=''
    while pila.getTam()!=0:
        val=pila.eliminarvalor()
        string+=str(val)
    print(string)






if __name__ == '__main__':
    num= int(input('Ingrese un numero en decimal: '))
    conversion(num)
