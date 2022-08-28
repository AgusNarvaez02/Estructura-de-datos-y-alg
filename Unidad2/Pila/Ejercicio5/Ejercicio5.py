class Pila:
    __lista=None

    def __init__(self):
        self.__lista= []

    def insertar(self, dato):
        self.__lista.append(dato)


    def tamaño(self):
        return len(self.__lista)

    def eliminarvalor(self):
        if len(self.__lista)==0:
            raise Exception('Lista vacia')

        valor = self.__lista.pop()
        return valor


class TorredeHanoi:
    __torre= list[Pila]
