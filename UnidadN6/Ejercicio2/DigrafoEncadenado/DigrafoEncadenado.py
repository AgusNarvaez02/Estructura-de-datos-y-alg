from Listaenlazada import Lista
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Registro:
    def __init__(self, nodo, conocido, distancia, camino):
        self.nodo= nodo
        self.conocido=conocido
        self.distancia= distancia
        self.camino=camino

class DigrafoEncaden:
    __vertices: np.array
    __matriz: np.array
    __pesos: np.array

    def __init__(self, vertices, aristas):
        self.__vertices = np.array(vertices)
        self.__matriz = np.full(len(vertices),None)

        for i in range(len(self.__matriz)):
            self.__matriz[i]= Lista()

        self.__pesos = np.full((len(vertices), len(vertices)), 1)

        for arista in aristas:
            i = self.HayVertice(arista[0])
            j = self.HayVertice(arista[1])

            self.__matriz[i].Insertar(j)


    def getPeso(self, ver1, ver2):
        return self.__matriz[self.HayVertice(ver1)][self.HayVertice(ver2)]

    def setPesos(self, pesos: list):
        for peso in pesos:
            self.__pesos[self.HayVertice(peso[0])][self.HayVertice(peso[1])] = peso[2]


    def HayVertice(self, vertice):
        for i in range(len(self.__vertices)):
            if self.__vertices[i] == vertice:
                return i
        raise Exception("Vertice inexistente")

    def Adycente(self, vertice):
        pos = self.HayVertice(vertice)
        lista = []
        for i in range(len(self.__vertices)):
            if self.__matriz[pos].Relacionado(i):
                lista.append(self.__vertices[i])
        return lista

    def CrearCamino(self, inicio, fin):
        visit = []
        pila = []
        pila.append(inicio)
        while len(pila) > 0:
            v = pila.pop()
            if v not in visit:
                visit.append(v)
                if v == fin:
                    return visit
            a = self.Adycente(v)
            for w in a:
                pila.append(w)

        return None

    def Camino(self, inicio, fin):
        self.HayVertice(inicio)
        self.HayVertice(fin)
        camino = self.CrearCamino(inicio, fin)
        if camino == None:
            print('No hay camino')
        else:
            return camino

    def Dijktra(self, Origen):
        Tabla = {}
        for vert in self.__vertices:
            Tabla[vert] = Registro(vert, False, 9999999999, None)
            Tabla[Origen].distancia = 0

        for i in range(len(self.__vertices)):
            v = None
            for vert in self.__vertices:
                if not Tabla[vert].conocido:
                    if v == None or Tabla[vert].distancia < Tabla[v].distancia:
                        v = vert

            Tabla[v].conocido = True

            for w in self.Adycente(v):
                if Tabla[v].distancia + self.getPeso(v, w) < Tabla[w].distancia:
                    Tabla[w].distancia = Tabla[v].distancia + self.getPeso(v, w)
                    Tabla[w].camino = v
        return Tabla

    def MinimoCamino(self, inicio, fin):
        try:
                self.HayVertice(inicio)
                self.HayVertice(fin)
                camino = self.Dijktra(inicio)
                if camino[fin] == None:
                    return 'Camino inexistente'

                else:
                    ver = fin
                    minimo = []

                    while ver != None:
                        minimo.append(ver)
                        ver = camino[ver].camino
                    minimo.reverse()
                    return minimo

        except:
            print('Alguno de los vertices no existe')

    def RecorridoenProfundidad(self, vinicial):
        vis = []
        pila = []
        pila.append(vinicial)
        while len(pila) > 0:
            ve = pila.pop()
            if ve not in vis:
                vis.append(ve)
                adyacentes = self.Adycente(ve)
                for w in adyacentes:
                    pila.append(w)
        return vis

    def Conexo(self):
        vis=[]
        pila=[]
        pila.append(self.__vertices[0])
        while len(pila)>0:
            v= pila.pop(0)
            if v not in vis:
                for elem in self.Adycente(v):
                    pila.append(elem)
        return len(vis)== len(self.__vertices)

    def grado(self, vertice):
        return len(self.Adycente(vertice))



    def RecorridoenAmplitud(self, vert):
        vis = []
        cola = []
        cola.append(vert)
        while len(cola) > 0:
            ve = cola.pop(0)
            if ve not in vis:
                vis.append(ve)
                adyacentes = self.Adycente(ve)
                for w in adyacentes:
                    cola.append(w)
        return vis
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
    nodos = [1, 2, 3, 4, 5]
    aristas = [(1, 3), (2, 3), (4, 3), (4, 5), (5, 1), (2,5)]
    digrafo = DigrafoEncaden(nodos, aristas)
    digrafo.grafico(nodos, aristas)
    print('Recorrido en profundidad: ', digrafo.RecorridoenProfundidad(1))
    print('Recorrido en amplitud: ', digrafo.RecorridoenProfundidad(1))

    print('Grado del vertice 1: ', digrafo.grado(1))

    print('El nodo 3 es sumidero: ', digrafo.NodoSumidero(3))
    print('El nodo 2 es Fuente: ', digrafo.NodoFuente(2))
    if digrafo.Conexo():
        print('El digrafo si es conexo')
    else:
        print('El digrafo NO es conexo')

