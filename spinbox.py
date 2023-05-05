from tkinter import *

root=Tk()
root.geometry("400x300")

w=Spinbox(root,values=("Python","HTML5","Java","Javascript"))
w.pack()

e=Spinbox(root,values=("Carne","Verdura","Pastas"))
e.pack()

root.mainloop()