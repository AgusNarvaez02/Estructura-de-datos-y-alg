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


def conversion(num):
    pila=Pila()
    while num>=1:
        resto = num % 2
        pila.insertar(resto)
        num= num//2
    string=''
    while pila.tamaño()!=0:
        val=pila.eliminarvalor()
        string+=str(val)
    print(string)






if __name__ == '__main__':
    num= int(input('Ingrese un numero en decimal: '))
    conversion(num)