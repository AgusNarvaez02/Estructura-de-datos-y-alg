import random
import numpy as np
class TablaH:
    __tamaño:int
    __tabla: np.array
    __aleatorio: int

    def __init__(self, tamaño, primo=False):
        if primo:
            self.__tamaño= self.NumPrimo(int(tamaño/0.7))
        else:
            self.__tamaño = tamaño
        self.__aleatorio= random.randint(1, self.__tamaño)
        self.__tabla=np.full(self.__tamaño,None)

    def NumPrimo(self, num):
        for i in range(2, num):
            if num % i == 0:
                return self.NumPrimo(num + 1)

        else:
            return num

    def hash(self, clave):
        return clave % self.__tamaño

    def PruePseudoRandom (self, clave):
        IndiceO= index= self.hash(clave)
        while self.__tabla[index]!= None and self.__tabla[index]!=clave:
            index= (index+self.__aleatorio) % self.__tamaño
            if index== IndiceO:
                return -1

        return index

    def Insertar(self, clave):
        indice= self.PruePseudoRandom(clave)

        if indice!=-1:
            self.__tabla[indice]=clave
        else:
            raise ValueError('Tabla llena')

    def Buscar(self, clave):
        indice= self.PruePseudoRandom(clave)
        if indice!=-1:
            return self.__tabla[indice]
        else:
            return None

    def longitudSecuenciaLineal(self, clave):
        index = self.hash(clave)
        cont=0
        while self.__tabla[index] != None and self.__tabla[index] != clave:
            index = (index + 1) % self.__tamaño
            cont+=1
        return cont

    def FactorCarga(self):
        tot= np.count_nonzero(self.__tabla!= None)
        return tot/self.__tamaño


if __name__ == '__main__':
    Tabl1= TablaH(1000, True)
    Tabl2= TablaH(1000)

    for i in range(1000):
        Tabl1.Insertar(random.randint(0,1000))
        Tabl2.Insertar(random.randint(0, 1000))
        print('Tabla 1, Numero primo ')
        print('Longitud secuencia de busqueda: ', Tabl1.longitudSecuenciaLineal(100))
        print('Factor de carga: {}'.format(Tabl1.FactorCarga()*1))

        print('Tabla 2 ')
        print('Longitud secuencia de busqueda: ', Tabl2.longitudSecuenciaLineal(100))
        print('Factor de carga: {}'.format(Tabl2.FactorCarga() * 1))
