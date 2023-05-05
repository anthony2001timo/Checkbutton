from tkinter import *

root=Tk()
texto=Text(root)
texto.pack()
texto.config(width=40,height=15,padx=15,pady=15,font=("arial,12"),selectbackground="blue")

label=Label(root,text="Escribe aqui")
label.pack()
label.config(bg="light blue",font="arial,20")

imagen=PhotoImage(file="C:\\Users\\Anthony Zambrano\\Desktop\\Python\\Interfaces Graficas\\Kiritokun.gif")
label1=Label(root,image=imagen)
label1.pack()

root.mainloop()