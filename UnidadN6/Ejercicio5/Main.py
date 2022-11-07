from DigrafoSecuencial import DigrafoSec

Ciudad:{
    'A': 'Almafuerte',
    'B': 'Belen',
    'C': 'Cordoba',
    'D': 'Dar-el-Salam',
    'E': 'Estambul',
    'F': 'Finisterre'}


def Buscar(ciudad):
    for vert in Ciudad:
        if Ciudad[vert].lower()== ciudad.lower():
            return vert

    return None

def getCamino(digrafo, vert1, vert2):
    Minimo= digrafo.caminoMinimo(vert1,vert2)
    retorna= ''
    for ciudad in Minimo:
        retorna+= Ciudad[ciudad] + '=>'

    return retorna[:-4]



if __name__== '__main__':
    vertice= ['A', 'B', 'C', 'D', 'E', 'F']
    adyacencias = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), ('B', 'F'), ('C', 'D'), ('D', 'B'), ('E', 'D'), ('E', 'F'), ('F', 'D'), ('F', 'A')]
    ciudad_inicio = Buscar(input("Ingrese ciudad de inicio(Almafuerte, Belen, Cordoba,Dar-el-Salam, Estambul y Finisterre): "))
    ciudad_destino = Buscar(input("Ingrese ciudad de destino(Almafuerte, Belen, Cordoba,Dar-el-Salam, Estambul y Finisterre): "))
    digrafo = DigrafoSec(vertice, adyacencias)
    print("El camino más corto entre las ciudades ", Ciudad[ciudad_inicio], "y", Ciudad[ciudad_destino], "es", getCamino(digrafo, ciudad_inicio, ciudad_destino))
    digrafo.grafico(vertice, adyacencias)
