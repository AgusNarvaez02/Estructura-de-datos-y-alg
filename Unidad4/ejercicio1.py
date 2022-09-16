from asyncio import streams


class Nodo:
    __izquierdo=None
    __dato:str
    __derecho=None

    def __init__(self, dato):
        self.__dato= dato
        self.__derecho=None
        self.__izquierdo=None
    

    def getdato(self):
        return self.__dato
    
    def getizq(self):
        return self.__izquierdo
    
    def getder(self):
        return self.__derecho
    
    def setizq(self, dato):
        self.__derecho=dato
    
    def setder(self, dato):
        self.__izquierdo=dato

    
    def insertarNodo(self, dato):
        if self.__dato==dato:
            raise Exception('Ya existe este dato')
        
        elif dato< self.__dato:
            if self.__izquierdo==None:
                self.__izquierdo= Nodo(dato)
            else: self.insertarNodo(dato)
        
        elif dato> self.__dato:
            if self.__derecho== None:
                self.__derecho=Nodo(dato)
            else:
                self.insertarNodo(dato)
    
    def NodoHoja(self):
        return self.__dato.getder()==None and self.__dato.getizq()==None
    
    def vacio(self):
        return self.__dato==None
    
    def Inorden(self):
        if self.getizq()!=None:
            self.__izquierdo.Inorden()
        print(self.__dato)
        if self.getder()!=None:
            self.__derecho.Inorden()
    
    def Preorden(self):
        print(self.__dato)
        if self.getizq()!=None:
            self.__izquierdo.Inorden()
        
        if self.getder()!=None:
            self.__derecho.Inorden()

    def PostOrden(self):
        if self.getizq()!=None:
            self.__izquierdo.Inorden()
        
        if self.getder()!=None:
            self.__derecho.Inorden()

        print(self.__dato)
            


class Arbol:
    __raiz:Nodo

    def __init__(self):
        self.__raiz= None
    

    def insertar(self, dato):
        if self.__raiz==None:
            self.__raiz= Nodo(dato)
        
        else:
            self.__raiz.insertarNodo(dato)
    


    def Inorden(self):
        if self.__raiz==None:
            raise Exception('Raiz vacia')
        else:
            self.__raiz.Inorden()
    
    def Preorden(self):
        if self.__raiz==None:
            raise Exception('Raiz vacia')
        else:
            self.__raiz.Preorden()





if __name__=='__main__':

    Raiz=Arbol()
    Raiz.insertar(4)
    Raiz.insertar(3)
    Raiz.insertar(5)
    Raiz.Inorden()
    Raiz.Preorden()



        
