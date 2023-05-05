from tkinter import*

root=Tk()
#Para colocar una imagen
imagen=PhotoImage(file="C:\\Users\\Anthony Zambrano\\Desktop\\Python\\Interfaces Graficas\\Kiritokun.gif")
label=Label(root,image=imagen)
label.pack()


"""
texto_nuevo=StringVar()
texto_nuevo.set("Python")

root.title("Bienvenidos")
root.config(width=400, height=300)
#Empezamos creando una variable y la llamamos label
label=Label(root, text="Hola mundo")
label.place(x=100,y=50)
label.config(bg="orange",fg="blue",font=("Arial",20))

label=Label(root, text="Bienvenidos")
label.place(x=40,y=100)
label.config(bg="light blue",fg="black",font=("Arial",20),textvariable=texto_nuevo)
"""
root.mainloop()

