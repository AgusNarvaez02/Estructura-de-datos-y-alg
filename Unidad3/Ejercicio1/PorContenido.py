import numpy as np
class Lista:
    __arreglo= None
    __tope= 0
    __tamaño: int


    def __init__(self, tamaño: int= 100):
        self.__arreglo= np.empty(tamaño, dtype=int)
        self.__tope= 0
        self.__tamaño= tamaño

    def __str__(self):
        return str(self.__arreglo[:self.__tope])

    def insertar(self, elemento):
        i=0
        if self.__tope== self.__tamaño:
            raise Exception('Lista llena ')


        while i<self.__tope and self.__arreglo[i]<=elemento:
            i+=1
        pos=i
        for i in range(self.__tope, pos, -1):
            self.__arreglo[i]= self.__arreglo[i-1]
        self.__arreglo[pos]= elemento
        self.__tope+=1



    def Listavacia(self):
        return self.__tope==0

    def Suprimir(self, pos):
        if self.__tope==0:
            raise Exception('Lista vacia')

        elemento= self.__arreglo[pos]
        for i in range(pos, self.__tope):
            self.__arreglo[i]= self.__arreglo[i+1]

        self.__tope-=1

        return elemento

    def Recuperar(self, pos):
        if self.__tope==0:
            raise Exception('Lista vacia')

        if self.__tope>pos:
            return self.__arreglo[pos]
        else:
            raise Exception

    def Siguiente(self, pos):
        if self.__tope == 0:
            raise Exception('Lista vacia')

        if self.__tope > pos+1:
            return self.__arreglo[pos+1]

    def Buscar(self, elemento):
        band= False
        i=0
        retorno= -1
        while i<self.__tope and band==False:
            if self.__arreglo[i]== elemento:
                band=True
                retorno= i
            else:
                i+=1
        return retorno

    def PrimerElemento(self):
        if self.__tope == 0:
            raise Exception('Lista vacia')
        return self.__arreglo[0]

    def UltimoElemento(self):
        if self.__tope == 0:
            raise Exception('Lista vacia')
        return self.__arreglo[self.__tope-1]

    def Anterior(self, pos):
        if self.__tope == 0:
            raise Exception('Lista vacia')
        if self.__tope > pos-1:
            return self.__arreglo[pos-1]

def ExtraerDeArchivo(self):
    lista=Lista()
    archivo = open('archivo.csv')
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        ob = Incendio(fila[0], fila[1])
        lista.insertar(ob)


if __name__ == '__main__':
    lista= Lista()
    lista.insertar(40)
    lista.insertar(30)
    lista.insertar(32)
    print(lista)
    print(lista.Suprimir(1))
    print(lista)
