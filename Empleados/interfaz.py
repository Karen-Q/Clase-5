from tkinter import *
from empleado import Empleado
from nomina import Nomina

class Ejercicio1:

    def __init__(self):
        root = Tk()

        frame = Frame(root)
        frame.pack()
        frame.config(bg="lightblue")
        frame.config(width= 500, height= 500)
        root.mainloop()

class Ejercicio2:

    def label1(self):
        root = Tk()
        Label(root, text="Hola mundo!").pack()
        Label(root, text="Otro Label!").pack()
        Label(root, text="Otro Label mas!").pack()
        Label(root, text="Label Final!").pack()
        root.mainloop()

    def label2(self):
        root = Tk()
        label = Label(root, text="Etiqueta a color!")
        label.pack(anchor=CENTER)
        label.config(fg="blue",
                     bg="green",
                     font=("Verdana",24))
        root.mainloop()

class Ejercicio3:

    def entrada1(self):
        root = Tk()
        entry = Entry(root)
        entry.pack()
        root.mainloop()
    
    def entrada2(self):
        root = Tk()
        entry = Entry(root)
        entry.pack(side=RIGHT)
        label = Label(root, text="Empleado")
        label.pack(side= LEFT)
        root.mainloop()

    def entrada3(self):
        root = Tk()
        frame1 = Frame(root)
        frame1.pack()

        entrada1 = Entry(frame1)
        entrada1.pack(side=RIGHT)

        label = Label(frame1, text="Nombres de los emprleados de la empresa")
        label.pack(side= LEFT)    

        frame2 = Frame(root)
        frame2.pack()  

        entrada1 = Entry(frame2)
        entrada1.pack(side=RIGHT)

        label = Label(frame2, text="Apellidos")
        label.pack(side= LEFT)    
        root.mainloop()

    def entrada4(self):
        root = Tk()
        label = Label(root, text="Nombres de los emprleados de la empresa")
        label.grid(row=0, column=0)

        entry = Entry(root)
        entry.grid(row=0,column=1)

        label2 = Label(root, text="apellidos")
        label2.grid(row=1, column=0)

        entry2 = Entry(root)
        entry2.grid(row=1,column=1)
        root.mainloop() 

class InterfazNomina:

    def __init__(self):
        self.root = Tk()
        self.root.config(bd=15)
        self.nombres = StringVar()
        self.apellidos = StringVar()
        self.cargo = StringVar()
        self.salario = StringVar()
        self.texto = Text(self.root)
        self.empleados = []

    def limpiar(self):
        self.nombres.set("")
        self.apellidos.set("")
        self.cargo.set("")
        self.salario.set("")


    def ingresar(self):
        empleado = Empleado()
        empleado.setNombre(self.nombres.get())
        empleado.setApellido(self.apellidos.get())
        empleado.setCargo(self.cargo.get())
        empleado.setSalario(self.salario.get())

        self.nomina = Nomina()
        self.nomina.setSalario(float(self.salario.get()))
        self.nomina.setDiasLiquidados(30)
        empleado.setNomina(self.nomina)  

        self.empleados.append(empleado)
        self.texto.delete(1.0,'end')

        for i in self.empleados:
            print(i)
            self.texto.insert('insert', i)
            self.texto.insert('insert', "\n\n")
        self.limpiar()



    def interfaz(self):
        frame = Frame(self.root, width= 480, height=320)

        #NOMBRES
        labelNombre = Label(frame, text="Nombre del empleado")
        labelNombre.grid(row=0,column=0)
        inputNombre = Entry(frame, textvariable=self.nombres)
        inputNombre.grid(row=0, column=1)
        #APELLIDOS
        labelApellido = Label(frame, text="Apellido del empleado")
        labelApellido.grid(row=1,column=0)
        inputApellido = Entry(frame, textvariable=self.apellidos)
        inputApellido.grid(row=1, column=1)
        #CARGO 
        labelCargo = Label(frame, text="Cargo")
        labelCargo.grid(row=2,column=0)
        inputCargo = Entry(frame, textvariable=self.cargo)
        inputCargo.grid(row=2, column=1)
        #SALARIO
        labelSalario = Label(frame, text="Salario")
        labelSalario.grid(row=3,column=0)
        inputSalario = Entry(frame, textvariable=self.salario)
        inputSalario.grid(row=3, column=1)

        agregar = Button(frame, text="Agregar", command=self.ingresar)
        agregar.grid(row=4, column=1)

        frame.pack(fill='both', expand=1)

        self.texto.pack(fill='both', expand=1)
        self.texto.config(padx=6, pady=4, bd=0, font=("Empleados", 12))
        self.root.mainloop()




