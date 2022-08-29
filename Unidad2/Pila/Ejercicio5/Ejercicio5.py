class Torre:
    __lista=None

    def __init__(self):
        self.__lista= []


    def vacio(self):
        return len(self.__lista)==0

    def añadirDisco(self, elemento):
        if self.vacio() or elemento<= self.__lista[-1]:
            print('ingresa al if')
            self.__lista.append(elemento)
        else:
            print('No puede colocar un disco mas grande encima de uno mas pequeño ')
            raise Exception('No puede colocar un disco mas grande encima de uno mas pequeño ')

    def tamaño(self):
        return len(self.__lista)


    def eliminarvalor(self):
        if len(self.__lista)==0:
            raise Exception('Lista vacia')

        valor = self.__lista.pop()
        return valor

    def TamañoDisco(self, i):
        if len(self.__lista)<i:
            return ' '

        return str(self.__lista[i-1])


