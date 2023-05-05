from tkinter import *

root=Tk()
imagen=PhotoImage()



frame=Frame(root, width=500,height=400)
frame.pack()

#Creacion del entry:
entry=Entry(frame)
entry.grid(row=0,column=1,padx=5,pady=5)

entry2=Entry(frame)
entry2.grid(row=1,column=1,padx=5,pady=5)

entry3=Entry(frame)
entry3.grid(row=2,column=1,padx=5,pady=5)
entry3.config(justify="center",show="*")

#Hacemos los labels:
label1=Label(frame, text="Nombre:")
label1.grid(row=0,column=0,sticky="w",padx=5,pady=5)

label2=Label(frame,text="Apellido:")
label2.grid(row=1,column=0,sticky="w",padx=5,pady=5)

label3=Label(frame,text="Password:")
label3.grid(row=2,column=0,sticky="w",padx=5,pady=5)

imagen=PhotoImage(file="C:\\Users\\Anthony Zambrano\\Desktop\\Python\\Interfaces Graficas\\Kiritokun.gif")
label4=Label(root,image=imagen)
label4.pack()

root.mainloop()
