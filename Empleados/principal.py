'''
from empleado import Empleado

e1 = Empleado()
e1.setNombre("Jonathan")
e1.apellido = "Campos Lozano"
e1.cargo = "Profesor"
e1.salario = "20000"

print(e1)

e2 = Empleado()
e2.setNombre("Maria")
e2.apellido = "Cardenas"
e2.cargo = "Gerente"
e2.salario = "5000000"

print(e2)


e3 = Empleado()
e3.setNombre("Camilo")
e3.apellido = "Cardenas"
e3.cargo = "Gerente 2"
e3.salario = "5000000"

print(e3)



e4 = Empleado()
e4.setNombre("Camilo")
e4.apellido = "Cardenas"
e4.cargo = "Gerente 2"
e4.salario = "5000000"

print(e4)


e5 = Empleado()
e5.setNombre("Camilo")
e5.apellido = "Cardenas"
e5.cargo = "Gerente 2"
e5.salario = "5000000"

print(e5)



e6 = Empleado()
e6.setNombre("Camilo")
e6.apellido = "Cardenas"
e6.cargo = "Gerente 2"
e6.salario = "5000000"

print(e6)
'''
'''
from indicadores import Indicadores

i = Indicadores()
print('TRM =', i.trm())
print('Salario Minimo =', i.salariominimo())
'''
'''
from nomina import Nomina

listaNomina =[]

while True:
    print("1. Calcular Nomina")
    print("10. salir")

    if input("Ingrese la opción") == "1":
        renglon = []
        n=Nomina()
        n.setSalario(2500000)
        n.setDiasLiquidados("30")

        renglon.append({'variable': 'Salario', 'resultado': n.getSalario()})
        renglon.append({'variable': 'Dias Liquidados', 'resultado': n.getDiasLiquidados()})
        renglon.append({'variable': 'Salario Devengado', 'resultado': n.salarioDevengado()})
        renglon.append({'variable': 'Auxilio de transporte', 'resultado': n.auxilioTransporte()})
        renglon.append({'variable': 'total devengado','resultado': n.totalDevengado()})

    elif input("Ingrese la opcion")== "10":
        print("Saliendo")
        break

    f=open('nomina_python.txt', 'w')

    for i in listaNomina:
        f.write('*******************\n')
        for j in i:
            f.write(str(j) + '\n')
    f.close()
'''
from interfaz import *

InterfazNomina().interfaz()
