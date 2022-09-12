from lista import Lista
import csv
class Designacion:
    __año:int
    __cargo:str
    __materia:str
    __genero:str

    def __init__(self, año, cargo, materia, genero):
        self.__año= año
        self.__cargo= cargo
        self.__materia= materia
        self.__genero= genero

    def getaño(self):
        return self.__año

    def getcargo(self):
        return self.__cargo

    def getmateria(self):
        return self.__materia

    def getgenero(self):
        return self.__genero


class Manejador:
    __lista= Lista

    def __init__(self, tam: int):
        self.__lista=Lista(tam)
    def carga(self):
        archivo = open('designaciones.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        c=0
        for fila in reader:
            ob = Designacion(fila[0],fila[1],fila[2],fila[3])
            self.__lista.insertar(c,ob)
            c+=1
            print(self.__lista)


    def buscar(self, cargo):
        if self.__lista.Listavacia():
            print('Lista Vacia')

        else:
            año= self.__lista.PrimerElemento().getaño()
            c=0
            for elem in self.__lista:
                if elem.getaño()!=año:
                    año= elem.getaño()
                    c=0

                if elem.getcargo()== cargo and elem.getgenero()=='Mujer':
                    c+=1

            print('Año: {}, Cantidad: {}'.format(elem.getaño(), c))



    def itemD(self, materia, cargo, año):
        c=0
        for desig in self.__lista:
            if desig.getmateria()==materia and desig.getcargo()==cargo and desig.año()==año:
                c+=1

        return c



if __name__ == '__main__':
    desig= Manejador(100)
    desig.carga()
    cargo= input('Ingrese un tipo de cargo: ')
    desig.buscar(cargo)
    materia=input('Materia: ')
    cargo=input('Cargo: ')
    año=input('Año: ')
    desig.itemD(materia,cargo,año)


