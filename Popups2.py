from tkinter import *
from tkinter import filedialog

root=Tk()

def abrir():
    archivo=filedialog.askopenfilename(title="Abrir",initialdir="Documentos",
    filetypes=(("Documento Texto","*.txt"),("Archivo Excel","*.xlsx")))
    print(archivo)

Button(root,text="Archivos",command=abrir).pack()



root.mainloop()