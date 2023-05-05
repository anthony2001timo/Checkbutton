from tkinter import *

root=Tk()
root.config(bd=20,bg="goldenrod3")
root.title("Casa de comidas")

def orden():
    lista=""
    if (queso.get()):
        lista +=" con queso"
    else:
        lista +=" sin queso"
    
    if (lechuga.get()):
        lista +=" y con lechuga"
    else:
        lista +=" y sin lechuga"

    imprimir.config(text=lista)

queso=IntVar()
lechuga=IntVar()

imagen=PhotoImage(file="C:\\Users\\Anthony Zambrano\\Desktop\\Python\\Interfaces Graficas\\hamburguesa_1.gif")
Label(root,image=imagen).pack(side=LEFT)

frame=Frame(root)
frame.pack(side=RIGHT)
frame.config(bg="goldenrod3")

Label(frame,text="¿Como quieres tu hamburguesa?",bg="goldenrod3",font="Curier 15").pack(anchor="w")
Checkbutton(frame,text="con queso",variable=queso,onvalue=1,offvalue=0,
bg="goldenrod3",font="Curier 10",command=orden).pack(anchor="w")

Checkbutton(frame,text="Con lechuga",variable=lechuga,onvalue=1,offvalue=0,
bg="goldenrod3",font="Curier 10",command=orden).pack(anchor="w")

imprimir=Label(frame,bg="goldenrod3")
imprimir.pack()
imprimir.config(font="Curier 10")

root.mainloop()