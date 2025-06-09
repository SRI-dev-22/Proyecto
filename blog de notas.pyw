import os
from tkinter import *
#desaparece los place y se sustituye por grid 
from tkinter import Tk, Label, Button, Entry, Frame, messagebox, Radiobutton, Text, Scrollbar, IntVar, filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *
#he puesto un geometry aqui 
root = Tk()
#alto y ancho de la ventana
alto = 900
ancho = 600
#calcula el acto y ancho de la ventana del escritorio “window” no es valido deberia ser mainframe
pantalla_alto = root.winfo_screenheight()
pantalla_ancho =  root.winfo_screenwidth()
#calcula las posiciones “x” e “y”
x = int((pantalla_alto /2) - (alto / 2))
y = int((pantalla_ancho /2) - (ancho / 2))
#ponemos el alto,ancho,x,y)
root.geometry("{}x{}+{}+{}".format( alto, ancho, x, y)) 
#este es mi icono, carga la ruta absoluta del icono, pero tiene que estar en la misma carpeta
icono_path = os.path.join(os.path.dirname(__file__), "icono.png")
#cargar el icono sin que se produca un error fatal
try:
    # lo guardo en una variable
    icono = PhotoImage(file=icono_path)
    #cargo la imagen
    root.iconphoto(False, icono)
except Exception:
    print("No se pudo cargar el icono:")
#la funcion donde esta guardar
def guardar(text_widget, ventana):
     #aqui aparece la ventana donde guarda, puedes decirle el nombre por defecto, la extension por defecto y el tipo de fichero que quieres guardar
    file = filedialog.asksaveasfilename(initialfile="untitled.txt",
                                        defaultextension=".txt",
                                        file=[("All Files", "*.*"),
                                              ("Text Documents", "*.txt")])
    if file is None:
        return
    elif file is (''):
         pass
    else:
        #prueba de errores por si falla
        try:
             ventana.title(os.path.basename(file))
             file = open(file, "w")
             file.write(text_widget.get(1.0, END))
        except Exception:
            print("No se pudo guardar el Archivo!")
        finally:
            file.close()
def abrir(text_widget, ventana):
    #aqui aparece la ventana donde guarda, puedes decirle el nombre por defecto, la extension por defecto y el tipo de fichero que quieres guardar
    file = askopenfilename(defaultextension=".txt",
                                    	file=[("All Files", "*.*"),
                                          	("Text Documents", "*.txt")])
    if file is None:
        return
    elif file is (''):
         pass
    else:
     try:
        ventana.title(os.path.basename(file))
        text_widget.delete(1.0, END)
        file = open(file, "r")
        text_widget.insert(1.0, file.read())
     except EXCEPTION:
        	print("No se pudo abrir el Archivo!")

def cerrar_ventana():
    """Cerrar la ventana principal y salir de la aplicación."""
    root.quit()  
    root.destroy()  

def abrir_ventana():
    nueva_ventana = Toplevel(root)
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("{}x{}+{}+{}".format(alto, ancho, x, y))
    
    menu_nuevo = Menu(nueva_ventana)
    nueva_ventana.config(menu=menu_nuevo)

    #puedes añadir widgets a esta nueva ventana
    p_aux = Frame(nueva_ventana)
    p_aux.pack(padx=10, pady=10, fill="both", expand=True)

    scroll = Scrollbar(p_aux)
    scroll.pack(side='right', fill='y')

    txtRes_nuevo = Text(p_aux, width=100, height=30, yscrollcommand=scroll.set)
    txtRes_nuevo.pack(side="left", fill="both", expand=True)

    scroll.config(command=txtRes.yview)  
    archivo_menu_nuevo = Menu(menu_nuevo, tearoff=0)
    menu_nuevo.add_cascade(label="Archivo", menu=archivo_menu_nuevo)
    archivo_menu_nuevo.add_command(label="Abrir", command=lambda: abrir(txtRes_nuevo, nueva_ventana))
    archivo_menu_nuevo.add_command(label="Guardar", command=lambda: guardar(txtRes_nuevo, nueva_ventana))
#menu Frame , llena x y lo posiciono encima
menu_principal = Menu(root)
root.config(menu=menu_principal)

#el menu principal
archivo_menu = Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Abrir", command=lambda: abrir(txtRes, root))
archivo_menu.add_command(label="Guardar", command=lambda: guardar(txtRes, root))
Editar_menu = Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Editar", menu=Editar_menu)
Editar_menu.add_command(label="Cerrar ventana", command=cerrar_ventana)
Editar_menu.add_command(label="Abrir ventana", command=abrir_ventana)
#cuadro de texto con scroll , mejorado con fill="both" y expand=True
p_aux = Frame(root)
p_aux.pack(padx=10, pady=10, fill="both", expand=True)

scroll = Scrollbar(p_aux)
scroll.pack(side='right', fill='y')

txtRes = Text(p_aux, width=100, height=30, yscrollcommand=scroll.set)
txtRes.pack(side="left", fill="both", expand=True)

scroll.config(command=txtRes.yview)

root.wm_title("Rewrite")
root.mainloop()