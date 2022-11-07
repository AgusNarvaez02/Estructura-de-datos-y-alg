from Lista import Lista
from numpy as np

class Tabla:
    __dimension: int
    __tabla: np.array
    __longitud: int

    def __init__(self, claves, primo=False):
        self.__dimension=int(claves/4)
        if primo:
            self.__dimension=self.NumPrimo(self.__dimension)
        self.__tabla=np.full(self.__dimension, None)
        self.__longitud=0

    def NumPrimo(self, num):
        for i in range(2, num):
            if num % i == 0:
                return self.NumPrimo(num + 1)
        else:
            return num

    def Insertar(self, valor):
        indice= self.MetodoPlegado(valor)
        if self.__tabla[indice]==None:
            self.__tabla[indice]= Lista()

        self.__tabla[indice].insertar(valor)

    def Bucar(self, valor):
        indice= self.MetodoPlegado(valor)
        nodo= self.__tabla[indice].bucar(valor)
        if nodo!= None:
            return nodo.getdato()
        else:
            return None

    def getLong(self):
        return self.__longitud

    def FactorCarga(self):
        tot= np.count_nonzero(self.__tabla!= None)
        return tot/self.__tamaño

    def Hash(self, clave):
        return clave % self.__dimension

    def MetodoPlegado(self, valor):
        valor= str(valor)
        res=0

        for i in range(0, len(valor), 2):
            if i+2<len(valor):
                res+=int(valor[i:i+2])
            else:
                res += int(valor[i:])
        if res>=self.__dimension:
            res= self.Hash(res)

        return res

    def long_clavesin(self):
        for i in range(self.__dimension):
            if self.__tabla[i]!= None and self.__tabla[i].getTamaño()>=2:
                print('Posicion de tabla: ',i)
                self.__tabla[i].Recorrer()
                print('Cantidad de datos en lista, ', self.__tabla[i].getTamaño())


    def Promedio(self):
        c=0
        prom=0
        for i in range(self.__dimension):
            if self.__tabla[i]!=None:
                c+= self.__tabla[i].getTamaño()
        prom= c/self.__dimension
        return prom


    def Inciso2(self):
        cont=0
        prom= self.Promedio()
        for i in range(self.__dimension):
            if self.__tabla[i]!=None:
                if abs(self.__tabla[i].getTamaño()-prom) >2:
                    cont+=1

        return cont

