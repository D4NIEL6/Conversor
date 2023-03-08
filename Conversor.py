#App para convertir pies a metros con Tkinter
#Daniel López Mendoza
#23/02/23

from tkinter import *
from tkinter import ttk

#Calse que hace las operaciones

class Conversor:
    
    def __init__(self, raiz): #el init sirve como constructor siempre se usa self
        raiz.title("Pies a Metros")

        self.pies=StringVar()
        self.metros=StringVar()

        
        #Es como un tipo liencio 
        #El pading es L,U,R,D(direccion en ingles)
        mainFarme= ttk.Frame(raiz,padding="12 10 12 10")
        mainFarme.grid(column=0, row=0)

        #Ingresar textos
        piesEntry=ttk.Entry(mainFarme, width=7, textvariable=self.pies)
        piesEntry.grid(column=1, row=0)
        #ttk.label(clase padre, texto).grid()
        ttk.Label(mainFarme, text="Pies").grid(column=2,row=0,sticky=W)
        ttk.Label(mainFarme, text="Son equivalentes a:").grid(column=0,row=1)
        ttk.Label(mainFarme, textvariable=self.metros).grid(column=1,row=1)
        ttk.Label(mainFarme, text="Metros").grid(column=2,row=1)

        #Boton
        ttk.Button(mainFarme, text="Calcular", command=self.calcular).grid(column=2,row=2)

        piesEntry.focus()
        #Operacion de enter
        raiz.bind("<Return>",self.calcular)  

    def calcular(self, *arg):
        print("Hi c:")
        piesUs=(self.pies.get()) #debuelbe la cadena 
        print("Pies ingresados:",piesUs)
        try:
            piesfus=float(piesUs) #cambia el valor
            metros=piesfus*0.3048
            print("Metros:",metros)
            self.metros.set(metros)
            self.pies.set("")
        except:
            print("Dato invalido...")



if __name__=="__main__":
    print("Este es el archivo principal.")
    print("Solo se mostrara esto si es el principal")