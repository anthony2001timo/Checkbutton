from tkinter import *

root=Tk()

root.geometry("400x400")

productos=Label(root, text="Productos",bg="light blue")
productos.pack()

def agregar():
    listaProductos.insert(END,entrada.get())


listaProductos=Listbox(root,width=50)

listaProductos.insert(0,"Carne")
listaProductos.insert(1,"Pollo")
listaProductos.insert(2,"Verdura")
listaProductos.insert(3,"Jugo")
listaProductos.pack()

#Eliminar productos:
#listaProductos.delete(0)

#Creacion del Entry:
entrada=Entry(root,bd=10)
entrada.pack()

#Creacion del boton:
boton=Button(root,text="Agregar producto",bd=10,command=agregar,bg="light green")
boton.pack()

root.mainloop()