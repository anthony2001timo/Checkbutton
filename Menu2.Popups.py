from tkinter import*
from tkinter import messagebox

def salir():
    i= messagebox.askquestion("Salir","¿Estas seguro que deseas salir?")
    if i== "yes":
     root.destroy()

def acerca():
   messagebox.showinfo("Informacion","Creado por Anthony Zambrano")

def licencia():
   messagebox.showinfo("Licencia","Producto licenciado hasta 2030")

def error():
   messagebox.showerror("Error","Se ha producido un error")

def deshacer():
   messagebox.askquestion("¿Estas seguro?","¿Desea deshacer todo?")

root=Tk()

barraMenu= Menu(root)
root.config(menu=barraMenu)

archivoMenu=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
archivoMenu.add_command(label="Nuevo archivo")
archivoMenu.add_command(label="Nueva ventana",command=error)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir",command=salir)


archivoEditar= Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Editar",menu=archivoEditar)
archivoEditar.add_command(label="Deshacer",command=deshacer )
archivoEditar.add_command(label="Rehacer")

archivoAyuda= Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)
archivoAyuda.add_command(label="Acerca de..",command=acerca)
archivoAyuda.add_command(label="Licencia",command=licencia)

root.mainloop()