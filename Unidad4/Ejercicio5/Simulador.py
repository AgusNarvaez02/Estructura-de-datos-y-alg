import random
from Monticulo import ColaDePrioridad

class Quirofano:
    __tiempoAct: int
    __libre: bool
    __TiempoAtencion: int


    def __init__(self):
        self.__tiempoAct=0
        self.__libre= True
        self.__tiempoAct=0

    def Ocupar(self):
        self.__libre=False

    def Libre(self):
        return self.__libre

    def TiempodeAtencion(self, tiempo):
        self.__TiempoAtencion= tiempo

    def actualizar(self):
        self.__tiempoAct+=1

        if self.__tiempoAct== self.__TiempoAtencion:
            self.__libre=True
            self.__TiempoAtencion=0
            self.__tiempoAct=0

class Simulador:
    __reloj: int
    __TiempodeSim: int
    __TiempoLLegada: int
    __ColaPacientes: ColaDePrioridad
    __Quirofano: Quirofano
    __TotaoPaci: int
    __TotalAtendidios: int

    def __init__(self):
        self.__reloj=0
        self.__TiempodeSim=60 *8
        self.__TiempoLLegada= 30
        self.__ColaPacientes= ColaDePrioridad(100)
        self.__Quirofano=Quirofano()
        self.__TotaoPaci=0
        self.__TotalAtendidios=0


    def LLegadadePaciente(self):
        num= random.random()
        if num<=(1/self.__TiempoLLegada):
            prioridad=random.randint(1,100)
            self.__ColaPacientes.Insertar(prioridad)
            if not self.__Quirofano.Libre():
                print('El paciente con prioridad ', prioridad, 'debe esperar')
            self.__TotaoPaci+=1
    def Atencion(self):
        if self.__Quirofano.Libre():
            if not self.__ColaPacientes.Vacio():
                prioridad= self.__ColaPacientes.Eliminar()
                self.__Quirofano.Ocupar()
                TiempodeAtencion= random.randint(60,120)
                self.__Quirofano.TiempodeAtencion(TiempodeAtencion)
                print('El paciente: ', prioridad ,'esta siendo atendidio ')
                self.__TotalAtendidios+=1
        else:
            self.__Quirofano.actualizar()
    def Simular(self):
        while self.__reloj<= self.__TiempodeSim:
            self.LLegadadePaciente()
            self.Atencion()
            self.__reloj+=1
            print('Cantidad Total de Pacientes: ', self.__TotaoPaci)
            print('Cantidad total de pacientes atendidos: ', self.__TotalAtendidios)
            print('pacientes que esperaron para ser atendidos: ', self.__TotaoPaci-self.__TotalAtendidios)

if __name__ == '__main__':
    Simulador= Simulador()
    Simulador.Simular()
