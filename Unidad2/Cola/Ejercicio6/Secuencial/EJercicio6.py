class Cola:
    __lista=None

    def __init__(self):
        self.__lista=[]


    def insertar(self, dato):
        self.__lista.append(dato)

    def tamaño(self):
        return len(self.__lista)

    def eliminar(self):
        if len(self.__lista)==0:
            raise Exception('Lista vacia')
        return self.__lista.pop(0)


if __name__ == '__main__':
    c=Cola()
    c.insertar(1)
    c.insertar(2)
    c.insertar(3)
    c.insertar(4)
    c.insertar(5)
    print(c.eliminar())
    print(c.eliminar())