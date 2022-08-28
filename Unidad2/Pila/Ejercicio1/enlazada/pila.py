from Enlazada import Nodo

class Pila:
    __cabeza= None
    __tamaño=0

    def __init__(self):
        self.__cabeza=None
        self.__tamaño=0

    def ingresar(self, dato):
        nodo = Nodo(dato)
        nodo.setnext(self.__cabeza)
        self.__cabeza = nodo
        self.__tamaño+=1

    def tamaño(self):
        return self.__tamaño

    def eliminar(self):

        if self.__cabeza== None:
            raise Exception('Cabeza vacia')
        aux = self.__cabeza
        self.__cabeza= self.__cabeza.getnetx()
        return aux.getdato()

if __name__ == '__main__':
    ob= Pila()
    ob.ingresar('FabriCapo')
    ob.ingresar('Aguss')
    print(ob.eliminar())



