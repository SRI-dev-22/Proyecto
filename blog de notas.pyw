import os
from tkinter import *
#desaparece los place y se sustituye por grid 
from tkinter import Tk, Label, Button, Entry, Frame, messagebox, Radiobutton, Text, Scrollbar, IntVar, filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *
# he puesto un geometry aqui 

root = Tk()
#alto y ancho de la ventana
alto = 900
ancho = 600
#calcula el acto y ancho de la ventana del escritorio “window” no es valido deberia ser mainframe
pantalla_alto = root.winfo_screenwidth()
pantalla_ancho =  root.winfo_screenheight()
#calcula las posiciones “x” e “y”
x = int((pantalla_alto /2) - (alto / 2))
y = int((pantalla_ancho /2) - (ancho / 2))
# ponemos el alto,ancho,x,y)
root.geometry("{}x{}+{}+{}".format( alto, ancho, x, y)) 
#root(fill="both", expand=True)
#root.widgets()

def noexiste(self):
        pass


# Menu Frame , llena x y lo posiciono encima
menu = Frame(root, width=900, height=30, bg="blue")
menu.pack(fill="x", side="top")

# Archivo Button , pongo el boton a la izquierda
btnarchivo = Button(menu, text="Archivo", command=noexiste, fg="green", bg="white")
btnarchivo.pack(side="left", padx=10)

# Cuadro de texto con scroll , mejorado con fill="both" y expand=True
p_aux = Frame(root)
p_aux.pack(padx=10, pady=10, fill="both", expand=True)

scroll = Scrollbar(p_aux)
scroll.pack(side='right', fill='y')

txtRes = Text(p_aux, width=100, height=30, yscrollcommand=scroll.set)
txtRes.pack(side="left", fill="both", expand=True)

scroll.config(command=txtRes.yview)


root.wm_title("Mi blog de Notas(Rewrite)")
root.mainloop()