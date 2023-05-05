#Empezamos importando la interfaz con el siguiente codigo:
from tkinter import *

#Despues creamos nuestra primera ventana:
root=Tk()

#Despues le colocamos un titulo
root.title("Timo")

#luego la modificamos para no poder mover la interfaz a lo alto o a lo ancho:
root.resizable(0,0)

#Le agregamos el icono en formato ico
root.iconbitmap("C:\\Users\\Anthony Zambrano\\Desktop\\Python\\Interfaces Graficas\\timoico.ico")

root.mainloop()