#desaparece los place y se sustituye por grid 
from tkinter import Tk, Label, Button, Entry, Frame, messagebox, Radiobutton, Text, Scrollbar, IntVar
# he puesto un geometry aqui 
class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("900x600")  
        self.pack(fill="both", expand=True)
        self.widgets()

    def noexiste(self):
        pass

    def widgets(self):
        # Menu Frame , llena x y lo posiciono encima
        menu = Frame(self, width=900, height=30, bg="blue")
        menu.pack(fill="x", side="top")

        # Archivo Button , pongo el boton a la izquierda
        self.btnarchivo = Button(menu, text="Archivo", command=self.noexiste, fg="green", bg="white")
        self.btnarchivo.pack(side="left", padx=10)

        # Cuadro de texto con scroll , mejorado con fill="both" y expand=True
        p_aux = Frame(self)
        p_aux.pack(padx=10, pady=10, fill="both", expand=True)

        scroll = Scrollbar(p_aux)
        scroll.pack(side='right', fill='y')

        self.txtRes = Text(p_aux, width=100, height=30, yscrollcommand=scroll.set)
        self.txtRes.pack(side="left", fill="both", expand=True)

        scroll.config(command=self.txtRes.yview)

root = Tk()
root.wm_title("Mi blog de Notas(Rewrite)")
app = MainFrame(root)
app.mainloop()