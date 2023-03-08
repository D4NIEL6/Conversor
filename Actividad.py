#App para convertir pies a metros con Tkinter
#Daniel López Mendoza
#07/03/23

from tkinter import *
from tkinter import ttk 

class Menu:
    def __init__(self, rut):
        rut.title("Inicio de secion")

        estruc=ttk.Frame(rut,padding="0 0 10 15")
        estruc.grid(column=0,row=0)


        ttk.Label(estruc, text="Usuario:",padding="10 10 5 10").grid(column=0,row=0,sticky=E)
        ttk.Label(estruc, text="Contraseña:",padding="10 10 5 15").grid(column=0,row=1)

        usu=ttk.Entry(estruc,width=25)
        usu.grid(column=1+2,row=0)
        con=ttk.Entry(estruc,width=25)
        con.grid(column=1+2,row=1)

        ttk.Button(estruc,text="Ingresar").grid(column=3,row=3,sticky=E)


raiz=Tk()
Menu(raiz)
raiz.mainloop()