from Grafo import GrafoSec

if __name__ == '__main__':

    vertices= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    adyacencias= [('1', '2'), ('1', '3'), ('1', '4'), ('2', '5'), ('2', '6'), ('3', '7'), ('3', '8'), ('4', '9'), ('4', '10')]

    graph= GrafoSec(vertices,adyacencias)
    criticos=[]

    for vertice in vertices:
        Nuevos= vertices.copy()
        Nuevos.remove(vertice)
        Adyacencias= []

        for ad in adyacencias:
            if vertice not in ad:
                Adyacencias.append(ad)

        subGrafo= GrafoSec(Nuevos, Adyacencias)

        if not subGrafo.Conexo():
            criticos.append(vertice)

    print('------------SITIOS CRITICOS---------------')
    print(criticos)
    print('-------Cantidad de sitios criticos----------')
    print(len(criticos))

    graph.grafico(vertices,adyacencias)
