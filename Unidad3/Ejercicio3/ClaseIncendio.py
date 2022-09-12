import csv
from ClaseLista import Lista

class Incendios:
    __provincia:str
    __hectareas:int

    def __init__(self, prov, hec):
        self.__provincia=prov
        self.__hectareas=int(hec)

    def getprovincia(self):
        return self.__provincia
    def getHectarea(self):
        return self.__hectareas

    def __gt__(self, otro):
        return self.__hectareas < otro.getHectarea()

class ManejadorIncendio:
    __Incendio: Lista

    def __init__(self, tam: int=100):
        self.__Incendio= Lista(tam)
    def carga(self):
        archivo = open('incendios.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            print(fila)
            ob = Incendios(fila[0],fila[1])
            self.__Incendio.insertar(ob)

    def mostrar(self):
        for i in range(0, self.__Incendio.getTope()):
            elem= self.__Incendio.Recuperar(i)
            print('Nombre de provincia: {} Superfie: {}' .format(elem.getprovincia(), elem.getHectarea()))

if __name__ == '__main__':
    Inc=ManejadorIncendio()
    Inc.carga()
    Inc.mostrar()

