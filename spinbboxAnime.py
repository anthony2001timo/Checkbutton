from tkinter import *
root=Tk()
root.geometry("400x300")

frame=Frame(root)
frame.config(bg="light blue")
frame.pack()

label=Label(root,text="Personajes de anime",bg="light blue").pack()


w=Spinbox(root,values=("Kirito","Inuyasha","Saito","Tsuna","Goku","Gohan","Natsu","Tetsuya","Kuroko"))
w.pack()

root.mainloop()