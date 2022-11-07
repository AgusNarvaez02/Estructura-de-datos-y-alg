import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Registro:
    def __init__(self, nodo, conocido, distancia, camino):
        self.nodo= nodo
        self.conocido=conocido
        self.distancia= distancia
        self.camino=camino

class DigrafoSec:
    __arreglo: np.array
    __vertices: int
    __pesos: np.array


    def __init__(self, vertices, aristas):
        self.__vertices = vertices
        self.__arreglo= np.full((len(self.__vertices), len(self.__vertices)), False)
        self.__pesos= np.full((len(self.__vertices),len(self.__vertices)),1)
        for arista in aristas:
            self.__arreglo[self.HayVertice(arista[0])][self.HayVertice(arista[1])]= True

    def getPeso(self, ver1, ver2):
        if self.HayVertice(ver1) and self.HayVertice(ver2):
            return self.__pesos[ver1][ver2]

    def setPesos(self, pesos: list):
        for peso in pesos:
            self.__pesos[self.HayVertice(peso[0])][self.HayVertice(peso[1])] = peso[2]

    def HayVertice(self,vertice):
        for i in range(len(self.__vertices)):
            if self.__vertices[i] == vertice:
                return i
        raise Exception("Vertice inexistente")

    def Adycente(self, vertice):
        pos= self.HayVertice(vertice)
        lista= []
        for i in range(len(self.__vertices)):
            if self.__arreglo[pos][i]:
                lista.append(self.__vertices[i])
        return lista

    def Camino(self, inicio, fin):
        visit= []
        pila=[]
        pila.append(inicio)
        while len(pila)>0:
            v=pila.pop()
            if v not in visit:
                visit.append(v)
                if v== fin:
                    return visit
            a= self.Adycente(v)
            for w in a:
                pila.append(w)

        return None



    def Dijktra(self,Origen):
        Tabla={}
        for vert in self.__vertices:
            Tabla[vert]= Registro(vert, False, 9999999999, None)
        Tabla[Origen].distancia=0

        for i in range(len(self.__vertices)):
            v= None
            for vert in self.__vertices:
                if not Tabla[vert].conocido:
                    if v == None or Tabla[vert].distancia < Tabla[v].distancia:
                        v= vert

            Tabla[v].conocido=True

            for w in self.Adycente(v):
                if Tabla[v].distancia + self.getPeso(v,w) < Tabla[w].distancia:
                    Tabla[w].distancia= Tabla[v].distancia + self.getPeso(v,w)
                    Tabla[w].camino=v
        return Tabla

    def MinimoCamino(self, inicio, fin):
        if self.HayVertice(inicio) and  self.HayVertice(fin):

            Tabla= self.Dijktra(inicio)
            camino=[]
            vert= fin
            while vert!=None:
                camino.append(vert)
                vert=Tabla[vert].camino
            camino.reverse()
            return camino


    def RecorridoenProfundidad(self, vinicial):
        vis=[]
        pila=[]
        pila.append(vinicial)
        while len(pila)>0:
            ve= pila.pop()
            if ve not in vis:
                vis.append(ve)
                adyacentes= self.Adycente(ve)
                for w in adyacentes:
                    pila.append(w)
        return vis


    def Conexo(self):
        conexo= False
        i=0
        while i<len(self.__vertices) and conexo==False:
            if len(self.RecorridoenProfundidad(self.__vertices[i]))< len(self.__vertices):
                conexo=True
            i+=1
        return conexo


    def grado(self, vertice):
        return len(self.Adycente(vertice))

    def mostrar(self):
        print(self.__arreglo)

    def RecorridoenAmplitud(self, vert):
        vis=[]
        cola=[]
        cola.append(vert)
        while len(cola)>0:
            ve=cola.pop(0)
            if ve not in vis:
                vis.append(ve)
                adyacentes = self.Adycente(ve)
                for w in adyacentes:
                    cola.append(w)
        return vis


    def Aciclico(self):
        vis = []
        pila = []
        pila.append(self.__vertices[0])
        while len(pila) > 0:
            ve = pila.pop()
            if ve not in vis:
                vis.append(ve)
                adyacentes = self.Adycente(ve)
                for w in adyacentes:
                    if w in vis:
                        return False
                    pila.append(w)
        return True

    def NodoSumidero(self, vertice):
        sumidero=False
        i=0
        while i<len(self.__vertices) and not sumidero:
            if vertice in self.Adycente(self.__vertices[i]):
                sumidero=True
            i+=1

        return len(self.Adycente(vertice))==0 and sumidero

    def NodoFuente(self, vertice):
        Fuente = True
        i = 0
        while i < len(self.__vertices) and Fuente:
            if vertice in self.Adycente(self.__vertices[i]):
                Fuente = True
            i += 1

        return len(self.Adycente(vertice))>0 and Fuente

    def grafico(self, vertices, adyacencia):
        G = nx.DiGraph()
        G.add_nodes_from(vertices)
        G.add_edges_from(adyacencia)
        nx.draw(G, with_labels=True)
        plt.show()

if __name__ == '__main__':
    vertices = [1, 2, 3, 4, 5, 6]
    aristas = [(1, 3), (2, 4), (5, 3), (6, 1), (6, 2), (5, 2), (3, 4)]
    Digrafo = DigrafoSec(vertices, aristas)
    Digrafo.grafico(vertices, aristas)
    print('Nodos adyacentes del vertice 1= ', Digrafo.Adycente(1))
    print('Grado del nodo 2= ', Digrafo.grado(2))
    print('Recorrido en profundidad con el nodo 1 de inicio= ', Digrafo.RecorridoenProfundidad(1))
    print('Recorrido en amplitud con el nodo 1 de inicio= ', Digrafo.RecorridoenAmplitud(1))

    if Digrafo.Conexo():
        print('El grafo si es conexo')
    else:
        print('El grafo NO es conexo')

    print('Camino Minimo entre los vertices 3 y 6: ', Digrafo.MinimoCamino(3, 6))
    Digrafo.grafico(vertices, aristas)
