from TablaHash import TablaHash
import random

if __name__ == '__main__':
    num=1000
    Buckets= 11
    cantBuckets= num/Buckets
    Tab1= TablaHash(cantBuckets, Buckets, True)
    Tab2 = TablaHash(cantBuckets, Buckets)

    for i in range(1000):
        Tab1.Insertar(random.randint(0, 1000))
        Tab2.Insertar(random.randint(0, 1000))
    print('Tabla con Numero Primo')
    Tab1.Mostrar()
    print('Tabla sin Numero Primo')
    Tab2.Mostrar()
