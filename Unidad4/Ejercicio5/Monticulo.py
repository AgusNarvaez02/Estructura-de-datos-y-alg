import numpy as np

class ColaDePrioridad:
    __arreglo: np.array
    __cantidad: int

    def __init__(self, tamaño):
        self.__arreglo= np.full(tamaño,None)
        self.__cantidad=0
        self.__arreglo[0]=-1

    def Vacio(self):
        return self.__cantidad==0

    def Lleno(self):
        return self.__cantidad== len(self.__arreglo)

    def Padre(self, pos):
        return pos//2

    def HijoDer(self, pos):
        return (pos*2) + 1

    def HijoIzq(self, pos):
        return pos*2

    def Hoja(self, pos):
        return pos > self.__cantidad

    def Intercambio(self, pos1, pos2):
        self.__arreglo[pos1],self.__arreglo[pos2]= self.__arreglo[pos2],self.__arreglo[pos1]


    def Insertar(self, elemento):
        if self.Lleno():
            return print('Cola llena')
        else:
            self.__cantidad+=1
            self.__arreglo[self.__cantidad]=elemento
            actual= self.__cantidad

            Padre= self.Padre(actual)
            while self.__arreglo[actual]< self.__arreglo[Padre]:
                self.Intercambio(actual, Padre)
                actual=Padre
                Padre= self.Padre(actual)

    def EliminarMinimo(self, pos):
        Padre= pos
        HijoIzq= self.HijoIzq(pos)
        HijoDer= self.HijoDer(pos)
        while not self.Hoja(HijoDer) and (self.__arreglo[Padre]> self.__arreglo[HijoDer] or self.__arreglo[HijoDer]):
            if self.__arreglo[HijoIzq]<= self.__arreglo[HijoDer]:
                self.Intercambio(Padre, HijoIzq)
                Padre=HijoIzq
            else:
                self.Intercambio(Padre, HijoDer)
                Padre = HijoDer

            HijoIzq= self.HijoIzq(Padre)
            HijoDer= self.HijoDer(Padre)

    def Eliminar(self):
        elimin= self.__arreglo[1]
        self.__arreglo[1]= self.__arreglo[self.__cantidad]
        self.__arreglo[self.__cantidad]=None
        self.__cantidad=-1
        self.EliminarMinimo(1)
        return elimin

