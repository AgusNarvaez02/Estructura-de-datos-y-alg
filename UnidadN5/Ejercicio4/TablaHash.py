import numpy as np

class Buckets:
    __arreglo: np.array
    __cant: int

    def __init__(self, tamañoB):
        self.__arreglo= np.full(tamañoB, None)
        self.__cant=0

    def insertar(self, dato):
        if self.__arreglo[-1] is not None:
            raise Exception('Bucket LLeno')
        else:
            self.__arreglo[self.__cant]=dato
            self.__cant+=1
    def getElemento(self, pos):
        return self.__arreglo[pos]

    def getTamaño(self):
        return self.__cant



class TablaHash:
    __tamaño:int
    __tabla: np.array
    __OverFlow:int
    __longitud:int


    def __init__(self, claves, buckets, primo=False):
        self.__tamaño= int(claves/0.7+1)

        if primo:
            self.__tamaño= self.primo(self.__tamaño)

        self.__longitud= len(str(self.__tamaño))
        self.__OverFlow= int(self.__tamaño*1.2)
        self.__tabla=np.empty(self.__OverFlow, dtype=Buckets)
        for i in range(self.__OverFlow):
            self.__tabla[i]= Buckets(buckets)


    def Insertar(self, dato):
        indice= self.metodoExtraccion(dato)
        self.__tabla[indice].insertar(dato)
    def Hash(self, dato):
        return dato % self.__tamaño

    def metodoExtraccion(self, dato):
        clave=str(dato)

        indice=int(clave[-self.__longitud])

        if indice>=self.__tamaño:
            indice= self.Hash(indice)
        return indice

    def primo(self, num):
        for i in range(2, num):
            if num % i == 0:
                return self.primo(num + 1)
        else:
            return num

    def Buscar(self, dato):
        indice= self.metodoExtraccion(dato)
        i=0
        retorno= None

        while i<self.__tabla[indice].getTamaño() and retorno==None:
            if self.__tabla[indice].getElemento(i)==dato:
                retorno=dato

            else:
                i+=1
        if i == self.__tabla[indice].getTamaño():
            i= self.__tamaño
            j=0

            while i<self.__OverFlow and retorno==None:
                if self.__tabla[i].getElemnto(j)== dato:
                    retorno= dato

                else:
                    j+=1
                    if j== self.__tabla[i].getTamaño():
                        j=0
                        i+=1
        return retorno


    def Mostrar(self):
        for j in range(self.__OverFlow):
            print('Bucket ', j ,'=', end= '')
            for i in range(self.__tabla[j].getTamaño()):
                print(self.__tabla[j].getTamaño(i), end= '')
                print()
