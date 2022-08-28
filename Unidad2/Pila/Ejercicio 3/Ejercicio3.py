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


def factorial(num):
    pila=Pila()
    val=num
    #pila.insertar(num)
    while num>1:
        resta=num-1
        pila.insertar(resta)
        print(resta)
        num=resta
    while pila.tamaño()!=0:
        val*=pila.eliminarvalor()
    print(val)




if __name__ == '__main__':
    num=int(input('Ingrese un numero: '))
    factorial(num)