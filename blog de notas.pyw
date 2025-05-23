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
# la funcion donde esta guardar
def guardar():
    #aqui aparece la ventana donde guarda, puedes decirle el nombre por defecto, la extension por defecto y el tipo de fichero que quieres guardar
    file = filedialog.asksaveasfilename(initialfile="untitled.txt",
                                        defaultextension=".txt",
                                        file=[("All Files", "*.*"),
                                              ("Text Documents", "*.txt")])
    if file is None:
        return
    else:
        # prueba de errores por si falla
        try:
             root.title(os.path.basename(file))
             file = open(file, "w")
             file.write(txtRes.get(1.0, END))
        except EXCEPTION:
            print("No se pudo guardar el Archivo!")
        finally:
            file.close
def guardar_como():
       pass
def abrir():
    #aqui aparece la ventana donde guarda, puedes decirle el nombre por defecto, la extension por defecto y el tipo de fichero que quieres guardar
    file = askopenfilename(defaultextension=".txt",
                                    	file=[("All Files", "*.*"),
                                          	("Text Documents", "*.txt")])
    try:
        root.title(os.path.basename(file))
        txtRes.delete(1.0, END)
        file = open(file, "r")
        txtRes.insert(1.0, file.read())
    except EXCEPTION:
        	print("No se pudo abrir el Archivo!")

def cerrar_ventana():
    """Cerrar la ventana principal y salir de la aplicación."""
    root.quit()  
    root.destroy()  

def abrir_ventana():
 root_top = Tk.Toplevel(root)
 root_top.title("nueva ventana")





# Menu Frame , llena x y lo posiciono encima
menu_principal = Menu(root)
root.config(menu=menu_principal)

#el menu principal
archivo_menu = Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Abrir", command=abrir)
archivo_menu.add_command(label="Guardar", command=guardar)
archivo_menu.add_command(label="Guardar como", command=guardar_como)
Editar_menu = Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Editar", menu=Editar_menu)
Editar_menu.add_command(label="Cerrar ventana", command=cerrar_ventana)
Editar_menu.add_command(label="abrir ventana", command=abrir_ventana)
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