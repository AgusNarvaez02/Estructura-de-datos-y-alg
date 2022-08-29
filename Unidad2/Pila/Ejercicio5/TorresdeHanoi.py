from Ejercicio5 import Torre

class TorresHanoi:
    __torres: list[Torre]
    __numDiscos: int

    def __init__(self, num):
        self.__torres = [Torre(), Torre(), Torre()]
        for i in range(num, 0, -1):
            self.__torres[0].añadirDisco(i)

        self.__numDiscos= num
    def moverDiscos(self, desde, hasta):
        try:
            valor= self.__torres[desde].eliminarvalor()
        except:
            return

        try:
            self.__torres[hasta].añadirDisco(valor)
        except:
            print('Ejecutooo')
            self.__torres[desde].añadirDisco(valor)


    def final(self):
        return self.__torres[2].tamaño()== self.__numDiscos

    def __repr__(self):
        string: str = '\n'

        for i in range(self.__numDiscos, 0, -1):
            string += '    {}|{}         {}|{}         {}|{}    \n'.format(
                self.__torres[0].TamañoDisco(i),
                self.__torres[0].TamañoDisco(i),
                self.__torres[1].TamañoDisco(i),
                self.__torres[1].TamañoDisco(i),
                self.__torres[2].TamañoDisco(i),
                self.__torres[2].TamañoDisco(i),
            )

        string += '=================================='

        return string

if __name__ == '__main__':
    cantidadDiscos= int(input('Ingrese cantidad de discos: '))
    juego= TorresHanoi(cantidadDiscos)

    while not juego.final():
        desde = int(input('Mover disco de torre: '))
        hasta = int(input('Hasta torre: '))

        if 1<=desde<=3 and 1<=hasta<=3:
            juego.moverDiscos(desde-1,hasta-1)
        else: print('Numero de torre fuera de rango, ingrese numero de torre 1 o 2 o 3 ')
        print(juego)



