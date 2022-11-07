from DigrafoSecuencial import DigrafoSec

Nombres= {
    'A': 'Ana',
    'B': 'Belen',
    'C': 'Cecilia',
    'D': 'Damiel',
    'E': 'Ezequiel',
    'F': 'Federico'}

def Camino(Digrafo, vert1, vert2):
    minimo= Digrafo.caminoMinimo(vert1, vert2)
    ret=" "
    for nom in minimo:
        ret+= Nombres[nom]+'=>'
    return ret

if __name__ == '__main__':
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    adyacencias = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), ('B', 'F'), ('C', 'D'), ('D', 'B'), ('E', 'D'),
                   ('E', 'F'), ('F', 'D'), ('F', 'A')]
    pesos = [('A', 'B', 3), ('A', 'D', 6), ('B', 'C', 1), ('B', 'E', 2), ('B', 'F', 1), ('C', 'D', 2), ('D', 'B', 3),
             ('E', 'D', 3), ('E', 'F', 2), ('F', 'D', 1), ('F', 'A', 5)]

    Digraph= DigrafoSec(vertices,adyacencias)
    Digraph.setPesos(pesos)
    for vert1 in vertices:
        for vert2 in vertices:
            if vert1 != vert2:
                print("*|* El camino más corto entre", Nombres[vert1], "y", Nombres[vert2], "es", Camino(Digraph, vert1, vert2), "*|*")

    Digraph.grafico(vertices, adyacencias)
