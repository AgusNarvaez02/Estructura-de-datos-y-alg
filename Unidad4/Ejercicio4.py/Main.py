
from CodificadorDecodificador import CodificadorDecodificador
from os import path

def Menu():
    print("1-- Ingrese el nombre del archivo a codificar \n2-- Generar archivo codificado en binario \n3-- Decodificar archivo en binario \n4-- Salir")

if __name__== "__main__":
    Menu()
    coddecod=CodificadorDecodificador()
    op=int(input("Ingrese una opcion(0 para finalizar): "))
    while op != 4:
        if op==1:
            nombre=input("Ingrese el nombre del archivo:")
            coddecod.Leerarchivo(nombre)
        elif op==2:
            coddecod.crearArbol()
            coddecod.comprimirArchivo()
        elif op==3:
            nombre=input("Ingrese el nombre del archivo a decodificar:")
            coddecod.descomprimirArchivo(nombre)
        else:
            print("Opcion no valida")
        Menu()
        op=int(input("Ingrese una opcion(0 para finalizar): "))
