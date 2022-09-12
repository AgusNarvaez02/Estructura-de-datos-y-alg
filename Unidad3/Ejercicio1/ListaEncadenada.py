class Nodo:
    __dato: str
    __siguiente= None

    def __init__(self, dato, sig):
        self.__dato= dato
        self.__siguiente= sig


    def getsiguiente(self):
        return self.__siguiente

    def setsiguiente(self, siguiente):
        self.__siguiente=siguiente

    def getDato(self):
        return self.__dato

class Lista:
    __cabeza: Nodo
    __tamaño:int


    def __init__(self):
        self.__cabeza= None
        self.__tamaño=0


    def getamaño(self):
        return self.__tamaño

    def Vacia(self):
        return self.__cabeza is None

    def __repr__(self):
        return str(lista(self))
    def Recuperar(self, pos):
        if 0>=pos-1>=self.__tamaño:
            raise Exception('posicion invalida')
        nodo=self.__cabeza
        for i in range(pos):
            nodo= nodo.getsiguiente()
        return nodo

    def insertar(self, dato, pos=0):
        if 0>=pos-1>=self.__tamaño:
            raise Exception('posicion invalida')

        self.__tamaño+=1

        if pos==0:
            self.__cabeza= Nodo(dato, self.__cabeza)
        else:
            p= self.Recuperar(pos-1)
            nodo= Nodo(dato, p.getsiguiente())
            p.setsiguiente(nodo)

    def eliminar(self, pos):
        if 0>=pos-1>=self.__tamaño:
            raise Exception('posicion invalida')
        self.__tamaño-=1

        if pos ==0:
            nodo= self.__cabeza
            self.__cabeza= nodo.getsiguiente()

        else:
            p= self.Recuperar(pos-1)
            nodo= p.getsiguiente()
            p.setsiguiente(nodo.getsiguiente())

        return nodo.getDato()


    def recuperar(self,pos):
        return self.Recuperar(pos).getDato()

    def buscar(self,d):
        nodo=self.__cabeza
        retorno=-1
        i=0
        while nodo is not None and nodo.getDato()!=d:
            nodo= nodo.getsiguiente()
            retorno=i
            i+=1
        return retorno

    def primerElemeno(self):
        if not self.Vacia():
            return self.__cabeza

    def UltimoElemento(self):
        if not self.Vacia():
            return self.Recuperar(self.getamaño()-1)




if __name__ == '__main__':
    lista=Lista()
    lista.insertar(2)
    lista.insertar(5,1)
    lista.insertar(4,2)
    lista.insertar(3,1)
    #print(lista)
    print(lista.eliminar(1))


