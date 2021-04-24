from indicadores import Indicadores

class Nomina(Indicadores):

    def __init__(self):
        self.__salarioBasico = 0
        self.__diasliquidados = 0
        self.__auxilio_Transporte =106454
        self.__smlv = self.salariominimo()

    def setSalario(self, salarioBasico):
        if str(type(salarioBasico)) =="<class 'float'>" or str(type(salarioBasico))=="<class'float'>":
            if self.__salarioBasico <= salarioBasico:
                self.__salarioBasico = salarioBasico
            else:
                print("El salario basico no puede ser inferior al SLMV vigente")
        else:
            print("Error")

        
    def getSalario(self):
        return self.__salarioBasico

    def setDiasLiquidados(self, diasLiquidados:int):
        self.__diasliquidados=diasLiquidados

    def getDiasLiquidados(self):
        return self.__diasliquidados

    def salarioDevengado(self):
        try:
            return (self.__salarioBasico/30)* self.__diasliquidados
        except:
            print("Error en alguna de las variables")

    def auxilioTransporte(self):
        if self.__salarioBasico >(self.__smlv * 2):
            return 0
        else:
            return (self.__auxilio_Transporte/30 * self.__diasliquidados)

    def totalDevengado(self):
        return self.salarioDevengado() + self.auxilioTransporte()


    def __str__(self):
        return str("salario Basico: {}"
                   "dias liquidados:{}"
                   "Auxilio de transporte:{}"
                   "Total Devengado:{}").format(
                       self.__salarioBasico,
                       self.__diasliquidados,
                       self.salarioDevengado(),
                       self.totalDevengado())