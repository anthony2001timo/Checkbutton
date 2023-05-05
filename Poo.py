import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #Configuracion de la ventana:
        self.title('Mi aplicacion')
        self.geometry('300x50')

        #Label:
        self.label= ttk.Label(self,text='Hola Tkinter')
        self.label.pack()

        #Creacion del boton:
        self.boton= ttk.Button(self,text='Haz click')
        self.boton['command'] = self.boton_accion
        self.boton.pack()

def boton_accion(self):
    showinfo(title='Informacion',message='Hola mundo')


if __name__== "__main__":
    app=App()
    app.mainloop()
