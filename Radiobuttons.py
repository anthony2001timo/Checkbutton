from tkinter import *

def mostrar():
    if opciones.get()==1:
        label2.config(text="Has elegido Masculino")
    else:
        label2.config(text="Has elegido Femenino")

root=Tk()

opciones=IntVar()

label1=Label(root,text="Elige un genero")
label1.pack()
label1.config(bd=5,bg="light blue")

Radiobutton(root,text="Masculino",variable=opciones,value=1,command=mostrar).pack()

Radiobutton(root,text="Femenino",variable=opciones,value=2,command=mostrar).pack()

label2=Label(root)
label2.pack()
label2.config(bg="light green")


root.mainloop()