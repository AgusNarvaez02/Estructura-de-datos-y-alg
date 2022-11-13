class Nodo:
    __dato: int
    __izquierdo: None
    __derecho: None

    def __init__(self, dato) -> None:
        self.__dato = dato
        self.__izquierdo = None
        self.__derecho = None

    def getdato(self):
        return self.__dato

    def getizq(self):
        return self.__izquierdo

    def getder(self):
        return self.__derecho

    def setizq(self, dato):
        self.__derecho = dato

    def setder(self, dato):
        self.__izquierdo = dato

    def setDato(self, dato):
        self.__dato= dato

    def HayDerecho(self):
        return self.__derecho!= None

    def HayIzquierdo(self):
        return self.__izquierdo!= None


class ArbolBinario:
    __raiz:Nodo

    def __init__(self)->None:
        self.__raiz=None

    def Vacio(self):
        return self.__raiz==None

    def getRaiz(self):
        return self.__raiz

    def MostrarDato(self):
        return self.__raiz.getdato()

    def Insertar(self,subArbol: Nodo,dato):
        print(dato)
        if subArbol == None:
            self.__raiz = Nodo(dato)

        else:
            if dato < subArbol.getdato():

                if subArbol.HayIzquierdo():
                    self.Insertar(subArbol.getizq(), dato)
                    print(dato)
                else:
                    subArbol.setizq(Nodo(dato))
            else:
                if subArbol.HayDerecho():
                    print('Derecho: ', dato)
                    self.Insertar(subArbol.getder(), dato)

                else:
                    subArbol.setder(Nodo(dato))

    def getGrado(self, subArbol):
        if not subArbol.HayDerecho() and not subArbol.HayIzquierdo():
            return 0
        if subArbol.HayIzquierdo() and not subArbol.HayDerecho():
            return 1
        if subArbol.HayIzquierdo() and subArbol.HayDerecho():
            return 2

    def Buscar(self, subArbol, dato):
        if subArbol== None:
            return None
        elif subArbol.getdato()== dato:
            return subArbol

        elif subArbol.getdato()> dato:
            return  self.Buscar(subArbol.getizq(), dato)
        else:
            return self.Buscar(subArbol.getder(), dato)

    def Nivel(self, subArbol, dato):
        if subArbol!= None:
            if subArbol.getdato()== dato:
                return 0

            elif subArbol.getdato()>dato:
                return self.Nivel(subArbol.getizq(), dato) + 1
            else:
                return self.Nivel(subArbol.getder(), dato) + 1
        else:
            return -1
    def MayorMenores(self, subArbol):
        if subArbol!=None:
            if subArbol.HayDerecho():
                return self.MayorMenores(subArbol.getder())
            else:
                return subArbol
        else:
            return None
    def Suprimir(self, subArbol:Nodo, dato, anterior=None):
        if subArbol!=None:
            if dato== subArbol.getdato():
                grado= self.getGrado(subArbol)
                if grado==0:
                    if anterior.getizq()==subArbol:
                        anterior.setizq(None)
                    else:
                        anterior.setder(None)
                elif grado==1:
                    if subArbol.HayIzquierdo():
                        hijo= subArbol.getizq()
                        if anterior.getder()== subArbol:
                            anterior.setder(hijo)
                        else:
                            anterior.setizq(hijo)
                        del subArbol
                    elif subArbol.HayDerecho():
                        hijo= subArbol.getder()
                        if anterior.getder()== subArbol:
                            anterior.setder(hijo)
                        else:
                            anterior.setizq(hijo)
                        del subArbol
                else:
                    mayorMenor = self.MayorMenores(subArbol.getizq())
                    self.Suprimir(self.__raiz, mayorMenor.getdato())
                    subArbol.setDato(menor.getdato())
            elif subArbol.getdato() > dato:
                self.Suprimir(subArbol.getizq(), dato, subArbol)
            else:
                self.Suprimir(subArbol.getder(), dato, subArbol)

        else:
            print('Dato erroneo')




    def PreOrden(self, subArbol):
        if subArbol!= None:
            print(subArbol.getdato())
            self.PreOrden(subArbol.getizq())
            self.PreOrden(subArbol.getder())
    def InOrden(self, subArbol):
        if subArbol != None:
            self.InOrden(subArbol.getizq())
            print(subArbol.getdato())
            self.InOrden(subArbol.getder())

    def PostOrden(self, subArbol):
        if subArbol != None:
            self.PostOrden(subArbol.getizq())
            self.PostOrden(subArbol.getder())
            print(subArbol.getdato())


    def Hoja(self, subArbol, dato):
        if subArbol!=None:
            if subArbol.getdato== dato:
                return not subArbol.HayIzquierdo() and not HayDerecho()

            else:
                if subArbol.getdato() > dato:
                    return self.Hoja(subArbol.getizq(), dato)
                else:
                    return self.Hoja(subArbol.getder, dato)

        else:
            return False

    def getHojo(self, subArbol, hijo, padre):
        Padre= self.Buscar(subArbol, padre)
        if Padre!=None:
            if hijo< padre:
                return Padre.getizq().getdato()== hijo
            else:
                return Padre.getder().getdato() == hijo
        else:
            return False

    def getPadre(self, subArbol, hijo):
        if subArbol!=None:
            if subArbol.getizq().getdato()== hijo:
                return subArbol
            elif subArbol.getder().getdato()==hijo:
                return subArbol
            else:
                if subArbol.getdato() > hijo:
                    return self.getPadre(subArbol.getizq(), hijo)
                else:
                    return self.getPadre(subArbol.getder(), hijo)
        else:
            raise Exception('Arbol vacio')

    def Altura (self, subArbol):
        if subArbol== None:
            return 0
        else:
            izq= self.Altura(subArbol.getizq())
            der= self.Altura(subArbol.getder())
            return max(izq, der)+1


    def FRONTERA(self, subArbol):
        if subArbol!=None:
            if subArbol.HayIzquierdo()==False and subArbol.HayDerecho()== False:
                print(subArbol.getdato())
            else:
                self.FRONTERA(subArbol.getizq())
                self.FRONTERA(subArbol.getder())

if __name__ == '__main__':
    ABB= ArbolBinario()
    ABB.Insertar(ABB.getRaiz(),70)
    raiz= ABB.getRaiz()
    ABB.Insertar(raiz, 35)
    ABB.Insertar(raiz, 40)
    ABB.Insertar(raiz, 5)
    ABB.Insertar(raiz, 100)
    print('Frontera')
    ABB.FRONTERA(raiz)

