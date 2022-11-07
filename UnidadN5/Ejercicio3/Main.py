from TablaHash import Tabla
import random
if __name__ == '__main__':
    Tabl1 = TablaH(1000, True)
    Tabl2 = TablaH(1000)

    for i in range(1000):
        Tabl1.Insertar(random.randint(0, 1000))
        Tabl2.Insertar(random.randint(0, 1000))
        print('Tabla 1, Numero primo ')
        print('Longitud dee cada una de las listas: ', Tabl1.long_clavein())
        print('Cantidad de Listas que registran una cantidad mayor o igual al promedio: ',Tabl1.Inciso2())

        print('Tabla 2 ')
        print('Longitud dee cada una de las listas: ', Tabl2.long_clavein())
        print('Cantidad de Listas que registran una cantidad mayor o igual al promedio: ', Tabl2.Inciso2())
