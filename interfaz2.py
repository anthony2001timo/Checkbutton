#Empezamos creando nuestra interfaz
from tkinter import *

root=Tk()

root.title("Timo")

root.resizable(1,1)

root.iconbitmap("C:\\Users\\Anthony Zambrano\\Desktop\\Python\\Interfaces Graficas\\timoico.ico")

#Le damos tamaño a nuestra ventana:
#root.geometry("600x350")

#Creamos un frame
myFrame= Frame(root)
myFrame.pack(fill="x",expand=1)
myFrame.pack(fill="y",expand=1)
myFrame.config(width=400,height=300)
myFrame.config(cursor="star")

#Ahora le agregamos color a nuestro frame:
myFrame.config(bg="blue")

#Ahora le agregamos un borde a nuestro frame:
myFrame.config(bd="20")

#Ahora le agregamos formato al borde:
myFrame.config(relief="sunken")

#Estos metodos los podemos utilizar si quisieramos mover nuestro frame
#myFrame.pack(side=LEFT)
#myFrame.pack(side=RIGHT)
#myFrame.pack(side=BOTTOM)
#myFrame.pack(side=RIGHT,anchor="n")
#myFrame.pack(fill="x")
#myFrame.pack(fill="y")
#myFrame.pack(fill="x",expand=1)
#myFrame.pack(fill="y",expand=1)

#Estos metodos tambien se los podemos colocar a nuestra ventana:
root.config(cursor="boat")
root.config(bg="orange")
root.config(bd="25")
root.config(relief="raised")
root.mainloop()