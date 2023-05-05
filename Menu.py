from tkinter import*

root=Tk()

barraMenu= Menu(root)
root.config(menu=barraMenu)

archivoMenu=Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
archivoMenu.add_command(label="Nuevo archivo")
archivoMenu.add_command(label="Nueva ventana")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir")


archivoEditar= Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Editar",menu=archivoEditar)
archivoEditar.add_command(label="Rehacer")

archivoAyuda= Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)
archivoAyuda.add_command(label="Acerca de..")
archivoAyuda.add_command(label="Licencia")

root.mainloop()
